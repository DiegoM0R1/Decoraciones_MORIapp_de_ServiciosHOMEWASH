# Generated by Django 5.0.4 on 2024-12-20 12:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EspecialidadPersonal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('sp_codigo', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('precio_base', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estado', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoServicio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('estado', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CalificacionServicio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('puntuacion', models.IntegerField()),
                ('comentario', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('estado', models.BooleanField(default=True)),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.venta')),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dni', models.CharField(max_length=20, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=20)),
                ('estado', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('especialidad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='services.especialidadpersonal')),
            ],
        ),
        migrations.CreateModel(
            name='DisponibilidadPersonal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('estado', models.BooleanField(default=True)),
                ('personal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.personal')),
            ],
        ),
        migrations.CreateModel(
            name='MaterialServicio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad_requerida', models.DecimalField(decimal_places=2, max_digits=10)),
                ('obligatorio', models.BooleanField(default=True)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.producto')),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.servicio')),
            ],
        ),
        migrations.AddField(
            model_name='servicio',
            name='tipo_servicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='services.tiposervicio'),
        ),
    ]
