# Generated by Django 4.2.1 on 2023-05-31 21:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_venta_detalle'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='oferta',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 31, 21, 44, 1, 781739, tzinfo=datetime.timezone.utc)),
        ),
    ]
