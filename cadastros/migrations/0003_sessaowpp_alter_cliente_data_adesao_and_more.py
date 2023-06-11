# Generated by Django 4.2.1 on 2023-06-09 22:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0002_alter_cliente_data_adesao_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SessaoWpp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=255)),
                ('token', models.CharField(max_length=255)),
                ('dt_inicio', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Sessão do WhatsApp',
                'verbose_name_plural': 'Sessões do WhatsApp',
            },
        ),
        migrations.AlterField(
            model_name='cliente',
            name='data_adesao',
            field=models.DateField(default=datetime.date(2023, 6, 9), verbose_name='Data de adesão'),
        ),
        migrations.AlterField(
            model_name='mensalidade',
            name='dt_vencimento',
            field=models.DateField(default=datetime.date(2023, 7, 9), verbose_name='Data do vencimento'),
        ),
    ]