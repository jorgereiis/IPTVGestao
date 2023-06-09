# Generated by Django 4.2 on 2023-07-06 20:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('cadastros', '0009_alter_cliente_data_adesao_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dadosbancarios',
            options={'verbose_name_plural': 'Dados Bancários'},
        ),
        migrations.AlterField(
            model_name='cliente',
            name='data_adesao',
            field=models.DateField(
                default=datetime.date(2023, 7, 6), verbose_name='Data de adesão'
            ),
        ),
        migrations.AlterField(
            model_name='mensalidade',
            name='dt_vencimento',
            field=models.DateField(
                default=datetime.date(2023, 8, 5), verbose_name='Data do vencimento'
            ),
        ),
    ]
