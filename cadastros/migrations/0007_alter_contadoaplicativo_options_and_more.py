# Generated by Django 4.2 on 2023-04-18 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0006_rename_sistema_aplicativo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contadoaplicativo',
            options={'verbose_name': 'Tipo de pagamento', 'verbose_name_plural': 'Tipos de pagamentos'},
        ),
        migrations.AlterField(
            model_name='contadoaplicativo',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True, unique=True, verbose_name='E-mail'),
        ),
    ]
