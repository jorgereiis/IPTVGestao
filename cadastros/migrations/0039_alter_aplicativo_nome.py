# Generated by Django 4.2.1 on 2023-05-09 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0038_alter_dispositivo_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aplicativo',
            name='nome',
            field=models.CharField(max_length=255),
        ),
    ]