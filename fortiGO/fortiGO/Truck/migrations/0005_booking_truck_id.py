# Generated by Django 2.1.2 on 2018-12-12 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Truck', '0004_cancellation_truck_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='truck_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='Truck.Trucks'),
        ),
    ]
