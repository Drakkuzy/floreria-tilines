# Generated by Django 4.2.1 on 2023-07-05 14:31

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0006_alter_venta_estado_alter_venta_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 5, 14, 31, 44, 133499, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='Suscrito',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('suscrito', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
