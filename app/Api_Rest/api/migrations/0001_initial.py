# Generated by Django 4.0.4 on 2022-04-14 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificador', models.CharField(max_length=100)),
                ('nombreArticulo', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
                ('unidades', models.CharField(max_length=100)),
                ('precioSnImuesto', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nPedido', models.CharField(max_length=100)),
                ('fechaCreacion', models.CharField(max_length=100)),
                ('precioSnImp', models.CharField(max_length=100)),
                ('porcentajeImp', models.CharField(max_length=100)),
                ('precioCnImuesto', models.CharField(max_length=100)),
                ('moneda', models.CharField(max_length=100)),
            ],
        ),
    ]