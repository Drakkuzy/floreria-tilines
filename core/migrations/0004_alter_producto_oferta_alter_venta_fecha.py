# Generated by Django 4.2.1 on 2023-05-31 23:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_producto_oferta_alter_venta_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='oferta',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 31, 23, 17, 16, 421064, tzinfo=datetime.timezone.utc)),
        ),
    ]
