# Generated by Django 2.1.2 on 2018-12-10 16:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Truck', '0002_routes_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cancellation',
            fields=[
                ('user_name', models.CharField(max_length=150)),
                ('user_email', models.CharField(max_length=150)),
                ('booking_id', models.IntegerField()),
                ('cancellation_id', models.AutoField(primary_key=True, serialize=False)),
                ('source', models.CharField(blank=True, choices=[('HYDERABAD', 'HYDERABAD'), ('CHENNAI', 'CHENNAI'), ('MUMBAI', 'MUMBAI'), ('BANGALORE', 'BANGALORE'), ('PUNE', 'PUNE'), ('SHAHBAD', 'SHAHBAD'), ('TANDUR', 'TANDUR'), ('RAICHUR', 'RAICHUR'), ('CUDDAPAH', 'CUDDAPAH'), ('ARAKKONAM', 'ARAKKONAM'), ('ADONI', 'ADONI'), ('HINDUPUR', 'HINDUPUR'), ('WARANGAL', 'WARANGAL'), ('VIJAYAWADA', 'VIJAYAWADA'), ('NELLORE', 'NELLORE'), ('KURNOOL', 'KURNOOL'), ('ANANTAPUR', 'ANANTAPUR'), ('GAURIBIDANUR', 'GAURIBIDANUR'), ('SHOLINGHUR', 'SHOLINGHUR'), ('AMBUR', 'AMBUR'), ('WHITEFIELD', 'WHITEFIELD')], default='HYDERABAD', help_text='Routes', max_length=30)),
                ('destination', models.CharField(blank=True, choices=[('HYDERABAD', 'HYDERABAD'), ('CHENNAI', 'CHENNAI'), ('MUMBAI', 'MUMBAI'), ('BANGALORE', 'BANGALORE'), ('PUNE', 'PUNE'), ('SHAHBAD', 'SHAHBAD'), ('TANDUR', 'TANDUR'), ('RAICHUR', 'RAICHUR'), ('CUDDAPAH', 'CUDDAPAH'), ('ARAKKONAM', 'ARAKKONAM'), ('ADONI', 'ADONI'), ('HINDUPUR', 'HINDUPUR'), ('WARANGAL', 'WARANGAL'), ('VIJAYAWADA', 'VIJAYAWADA'), ('NELLORE', 'NELLORE'), ('KURNOOL', 'KURNOOL'), ('ANANTAPUR', 'ANANTAPUR'), ('GAURIBIDANUR', 'GAURIBIDANUR'), ('SHOLINGHUR', 'SHOLINGHUR'), ('AMBUR', 'AMBUR'), ('WHITEFIELD', 'WHITEFIELD')], default='HYDERABAD', help_text='Routes', max_length=30)),
                ('load_weight', models.IntegerField(choices=[(250, 250), (500, 500), (750, 750), (1000, 1000)])),
                ('date_booked', models.CharField(max_length=150)),
                ('date_journey', models.CharField(max_length=150)),
                ('date_cancelled', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
