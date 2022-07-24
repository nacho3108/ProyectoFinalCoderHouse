# Generated by Django 4.0.6 on 2022-07-24 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razonSocial', models.CharField(max_length=50)),
                ('cuit', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('provincia', models.CharField(max_length=50)),
                ('codigoPostal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Fabrica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razonSocial', models.CharField(max_length=50)),
                ('cuit', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('provincia', models.CharField(max_length=50)),
                ('codigoPostal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Hilado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoColor', models.IntegerField()),
                ('partida', models.IntegerField()),
                ('ordenPedido', models.IntegerField()),
            ],
        ),
    ]
