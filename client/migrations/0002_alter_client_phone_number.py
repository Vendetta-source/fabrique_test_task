# Generated by Django 4.1.3 on 2022-11-30 13:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='phone_number',
            field=models.PositiveBigIntegerField(validators=[django.core.validators.RegexValidator(message='Номер телефона клиента в формате 7XXXXXXXXXX', regex='^7\\w{8,15}$')], verbose_name='Номер телефона'),
        ),
    ]
