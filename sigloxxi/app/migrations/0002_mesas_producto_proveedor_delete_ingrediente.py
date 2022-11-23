# Generated by Django 4.1.3 on 2022-11-23 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='mesas',
            fields=[
                ('id_mesa', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=80)),
                ('max_pers', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_prod', models.AutoField(primary_key=True, serialize=False)),
                ('nom_prod', models.CharField(max_length=50)),
                ('stock', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
                ('valor', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='proveedor',
            fields=[
                ('id_prov', models.AutoField(primary_key=True, serialize=False)),
                ('nom_prov', models.CharField(max_length=50)),
                ('mail', models.CharField(max_length=50)),
                ('fono', models.IntegerField()),
                ('direccion', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Ingrediente',
        ),
    ]
