# Generated by Django 5.0.4 on 2024-12-20 12:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoTransaccion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaccion',
            fields=[
                ('codigo_transaccion', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('descripcion', models.TextField()),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_transaccion', models.DateTimeField()),
                ('api_response', models.TextField(blank=True, null=True)),
                ('estado', models.BooleanField(default=True)),
                ('tipo_transaccion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='transactions.tipotransaccion')),
            ],
        ),
    ]
