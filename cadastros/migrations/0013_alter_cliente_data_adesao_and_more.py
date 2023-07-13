# Generated by Django 4.2.1 on 2023-07-12 21:29

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cadastros', '0012_alter_cliente_data_adesao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='data_adesao',
            field=models.DateField(default=datetime.date(2023, 7, 12), verbose_name='Data de adesão'),
        ),
        migrations.AlterField(
            model_name='mensalidade',
            name='dt_vencimento',
            field=models.DateField(default=datetime.date(2023, 8, 11), verbose_name='Data do vencimento'),
        ),
        migrations.CreateModel(
            name='HorarioEnvios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.TimeField()),
                ('ativo', models.BooleanField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Horário de Envio',
                'verbose_name_plural': 'Horarios de Envio',
            },
        ),
    ]
