# Generated by Django 2.1.2 on 2018-12-12 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Truck', '0005_booking_truck_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='truck_id',
        ),
    ]
