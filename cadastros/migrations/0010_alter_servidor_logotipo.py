# Generated by Django 4.2 on 2023-04-20 21:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cadastros", "0009_servidor_logotipo_alter_cliente_data_adesao_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="servidor",
            name="logotipo",
            field=models.CharField(max_length=255),
        ),
    ]
