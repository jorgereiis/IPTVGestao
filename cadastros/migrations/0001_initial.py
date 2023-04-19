# Generated by Django 4.2 on 2023-04-18 12:10

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=15)),
                ('data_pagamento', models.IntegerField(blank=True, default=None, null=True, verbose_name='Data de pagamento')),
                ('data_adesao', models.DateField(default=datetime.date(2023, 4, 18), verbose_name='Data de adesão')),
                ('data_cancelamento', models.DateField(blank=True, null=True, verbose_name='Data de cancelamento')),
                ('ultimo_pagamento', models.DateField(blank=True, null=True, verbose_name='Último pagamento realizado')),
                ('cancelado', models.BooleanField(default=False, verbose_name='Cancelado')),
            ],
        ),
        migrations.CreateModel(
            name='Dispositivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, unique=True)),
                ('modelo', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plano',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(choices=[('Mensal', 'Mensal'), ('Semestral', 'Semestral'), ('Anual', 'Anual')], default='Mensal', max_length=255, unique=True, verbose_name='Nome do plano')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Valor')),
            ],
        ),
        migrations.CreateModel(
            name='PlanoIndicacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('tipo_plano', models.CharField(choices=[('desconto', 'Desconto na mensalidade'), ('dinheiro', 'Valor em dinheiro')], max_length=10)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=6)),
                ('ativo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Planos de Indicação',
            },
        ),
        migrations.CreateModel(
            name='Qtd_tela',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telas', models.PositiveSmallIntegerField(unique=True, verbose_name='Quantidade de telas')),
            ],
            options={
                'verbose_name_plural': 'Quantidade de telas',
            },
        ),
        migrations.CreateModel(
            name='Servidor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Servidores',
            },
        ),
        migrations.CreateModel(
            name='Sistema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tipos_pgto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(choices=[('PIX', 'PIX'), ('Cartão de Crédito', 'Cartão de Crédito'), ('Boleto', 'Boleto')], default='PIX', max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Tipo de pagamento',
                'verbose_name_plural': 'Tipos de pagamentos',
            },
        ),
        migrations.CreateModel(
            name='Mensalidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, default=None, max_digits=5, verbose_name='Valor')),
                ('dt_vencimento', models.DateField(default=datetime.date(2023, 5, 18), verbose_name='Data de vencimento')),
                ('dt_pagamento', models.DateField(blank=True, default=None, null=True, verbose_name='Data de pagamento')),
                ('pgto', models.BooleanField(default=False, verbose_name='Pago')),
                ('cancelado', models.BooleanField(default=False)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.cliente')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='dispositivo',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='cadastros.dispositivo'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='forma_pgto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cadastros.tipos_pgto', verbose_name='Forma de pagamento'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='indicado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cadastros.cliente'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='plano',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cadastros.plano'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='servidor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.servidor'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='sistema',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='cadastros.sistema'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='telas',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cadastros.qtd_tela'),
        ),
    ]
