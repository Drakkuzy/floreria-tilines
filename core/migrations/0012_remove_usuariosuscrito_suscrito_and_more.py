# Generated by Django 4.2.1 on 2023-07-05 23:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_usuariosuscrito_correo_suscrito_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuariosuscrito',
            name='suscrito',
        ),
        migrations.RemoveField(
            model_name='usuariosuscrito',
            name='usuario',
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 5, 23, 9, 15, 291651, tzinfo=datetime.timezone.utc)),
        ),
    ]
