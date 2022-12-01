from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger


class MailingList(models.Model):
    start_datetime = models.DateTimeField(verbose_name='Дата и время начала рассылки')
    message = models.TextField(verbose_name='Сообщение')
    phone_code_filter = models.PositiveIntegerField(verbose_name='Код мобильного оператора',
                                                    blank=True)
    tag_filter = models.CharField(verbose_name='Тeг',
                                  max_length=50,
                                  blank=True)
    end_datetaime = models.DateTimeField(verbose_name='Дата и время окончания рассылки')

    @property
    def to_send(self):
        now = timezone.now()
        if self.start_datetime <= now <= self.end_datetaime:
            return True
        else:
            return False

    def __str__(self):
        return f'{self.message}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


from .external_service import send


def scedule_mailing(sender, instance, signal, *args, **kwargs):
    scheduler = BackgroundScheduler()
    if instance.to_send:
        scheduler.add_job(
            send,
            trigger='date',
            run_date=timezone.now(),
            args=[instance.pk],
            coalesce=True,
            max_instances=1,
            replace_existing=True,
        )
    else:
        scheduler.add_job(
            send,
            trigger='date',
            run_date=instance.start_datetime,
            args=[instance.pk],
            coalesce=True,
            max_instances=1,
            replace_existing=True,
        )
    scheduler.start()


post_save.connect(scedule_mailing, sender=MailingList)
