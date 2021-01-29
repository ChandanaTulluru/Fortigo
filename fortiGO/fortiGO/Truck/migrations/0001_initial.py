# Generated by Django 2.1.2 on 2018-12-08 13:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('user_name', models.CharField(max_length=150)),
                ('user_email', models.CharField(max_length=150)),
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('source', models.CharField(blank=True, choices=[('HYDERABAD', 'HYDERABAD'), ('CHENNAI', 'CHENNAI'), ('MUMBAI', 'MUMBAI'), ('BANGALORE', 'BANGALORE'), ('PUNE', 'PUNE'), ('SHAHBAD', 'SHAHBAD'), ('TANDUR', 'TANDUR'), ('RAICHUR', 'RAICHUR'), ('CUDDAPAH', 'CUDDAPAH'), ('ARAKKONAM', 'ARAKKONAM'), ('ADONI', 'ADONI'), ('HINDUPUR', 'HINDUPUR'), ('WARANGAL', 'WARANGAL'), ('VIJAYAWADA', 'VIJAYAWADA'), ('NELLORE', 'NELLORE'), ('KURNOOL', 'KURNOOL'), ('ANANTAPUR', 'ANANTAPUR'), ('GAURIBIDANUR', 'GAURIBIDANUR'), ('SHOLINGHUR', 'SHOLINGHUR'), ('AMBUR', 'AMBUR'), ('WHITEFIELD', 'WHITEFIELD')], default='HYDERABAD', help_text='Routes', max_length=30)),
                ('destination', models.CharField(blank=True, choices=[('HYDERABAD', 'HYDERABAD'), ('CHENNAI', 'CHENNAI'), ('MUMBAI', 'MUMBAI'), ('BANGALORE', 'BANGALORE'), ('PUNE', 'PUNE'), ('SHAHBAD', 'SHAHBAD'), ('TANDUR', 'TANDUR'), ('RAICHUR', 'RAICHUR'), ('CUDDAPAH', 'CUDDAPAH'), ('ARAKKONAM', 'ARAKKONAM'), ('ADONI', 'ADONI'), ('HINDUPUR', 'HINDUPUR'), ('WARANGAL', 'WARANGAL'), ('VIJAYAWADA', 'VIJAYAWADA'), ('NELLORE', 'NELLORE'), ('KURNOOL', 'KURNOOL'), ('ANANTAPUR', 'ANANTAPUR'), ('GAURIBIDANUR', 'GAURIBIDANUR'), ('SHOLINGHUR', 'SHOLINGHUR'), ('AMBUR', 'AMBUR'), ('WHITEFIELD', 'WHITEFIELD')], default='HYDERABAD', help_text='Routes', max_length=30)),
                ('load_weight', models.IntegerField(choices=[(250, 250), (500, 500), (750, 750), (1000, 1000)])),
                ('date_booked', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_journey', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Drivers',
            fields=[
                ('driver_id', models.AutoField(primary_key=True, serialize=False)),
                ('driver_name', models.CharField(max_length=150)),
                ('driver_mobile', models.CharField(max_length=150)),
                ('driver_email', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating_Q1', models.IntegerField()),
                ('rating_Q2', models.IntegerField()),
                ('rating_Q3', models.IntegerField()),
                ('rating_Q4', models.IntegerField()),
                ('text_Q1', models.TextField()),
                ('text_Q2', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('date_payment', models.DateTimeField(default=django.utils.timezone.now)),
                ('email', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150)),
                ('date', models.CharField(max_length=150)),
                ('purpose', models.TextField(max_length=300)),
                ('duration', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RentalTrucks',
            fields=[
                ('truck_id', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('max_load', models.IntegerField()),
                ('driver_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Truck.Drivers')),
            ],
        ),
        migrations.CreateModel(
            name='Routes',
            fields=[
                ('routeid', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('start', models.CharField(max_length=150)),
                ('int_st2', models.CharField(max_length=150)),
                ('int_st3', models.CharField(max_length=150)),
                ('int_st4', models.CharField(max_length=150)),
                ('end', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Truck_status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starting_date', models.CharField(max_length=150)),
                ('arriving_date', models.CharField(max_length=150)),
                ('truck_weight', models.IntegerField()),
                ('route_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Truck.Routes')),
            ],
        ),
        migrations.CreateModel(
            name='Trucks',
            fields=[
                ('truck_id', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('max_load', models.IntegerField()),
                ('driver_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Truck.Drivers')),
                ('route_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Truck.Routes')),
            ],
        ),
        migrations.CreateModel(
            name='UserLog',
            fields=[
                ('userlogid', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('pincode', models.IntegerField()),
                ('date_registered', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='truck_status',
            name='truck_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Truck.Trucks'),
        ),
    ]