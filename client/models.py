from django.core.validators import RegexValidator
from django.db import models


# Create your models here.
class Client(models.Model):
    phone_regex = RegexValidator(regex=r'^7\w{8,15}$',
                                 message="Номер телефона клиента в формате 7XXXXXXXXXX")
    phone_number = models.PositiveBigIntegerField(verbose_name='Номер телефона', validators=[phone_regex])
    phone_code = models.PositiveIntegerField(verbose_name='Код мобильного оператора')
    tag = models.CharField(verbose_name='Тeг', max_length=50, blank=True)
    time_zone = models.CharField(verbose_name='Часовой пояс', max_length=10)

    def __str__(self):
        return f'Клиент {self.pk} с номером {self.phone_number}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
