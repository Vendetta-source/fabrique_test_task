from django.db import models
from mailing_list.models import MailingList
from client.models import Client


class Message(models.Model):
    datetime_creation = models.DateTimeField(verbose_name='Дата создания',
                                             auto_now_add=True)
    status = models.CharField(verbose_name='Статус отправки',
                              max_length=15,
                              choices=(('sent', 'sent'),
                                       ('failed', 'failed'),
                                       ('proceeded', 'proceeded')))
    message = models.ForeignKey(MailingList, on_delete=models.CASCADE, related_name='messages')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='messages')

    def __str__(self):
        return f'Сообщение {self.pk} для {self.message} для {self.client}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
