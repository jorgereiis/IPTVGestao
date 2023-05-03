# Generated by Django 4.2 on 2023-05-03 09:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('cadastros', '0023_remove_planoindicacao_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='data_adesao',
            field=models.DateField(
                default=datetime.date(2023, 5, 3), verbose_name='Data de adesão'
            ),
        ),
        migrations.AlterField(
            model_name='mensalidade',
            name='dt_vencimento',
            field=models.DateField(
                default=datetime.date(2023, 6, 2), verbose_name='Data do vencimento'
            ),
        ),
    ]
