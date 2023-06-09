# Generated by Django 4.2.1 on 2023-06-30 16:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0005_alter_cliente_data_adesao_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecretTokenAPI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Secret Token API',
                'verbose_name_plural': 'Secrets Tokens API',
            },
        ),
        migrations.AlterField(
            model_name='cliente',
            name='data_adesao',
            field=models.DateField(default=datetime.date(2023, 6, 30), verbose_name='Data de adesão'),
        ),
        migrations.AlterField(
            model_name='mensalidade',
            name='dt_vencimento',
            field=models.DateField(default=datetime.date(2023, 7, 30), verbose_name='Data do vencimento'),
        ),
    ]
