# Generated by Django 4.2.1 on 2023-09-18 21:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0016_alter_cliente_data_adesao_alter_cliente_telefone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contadoaplicativo',
            name='verificado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='data_adesao',
            field=models.DateField(default=datetime.date(2023, 9, 18), verbose_name='Data de adesão'),
        ),
        migrations.AlterField(
            model_name='mensalidade',
            name='dt_vencimento',
            field=models.DateField(default=datetime.date(2023, 10, 18), verbose_name='Data do vencimento'),
        ),
    ]
