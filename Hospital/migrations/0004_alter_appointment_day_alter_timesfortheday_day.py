# Generated by Django 4.1.6 on 2023-02-24 08:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0003_alter_appointment_day_alter_timesfortheday_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='day',
            field=models.DateField(default=datetime.date(2023, 2, 24)),
        ),
        migrations.AlterField(
            model_name='timesfortheday',
            name='day',
            field=models.DateField(default=datetime.date(2023, 2, 24)),
        ),
    ]
