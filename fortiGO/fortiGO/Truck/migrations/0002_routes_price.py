# Generated by Django 2.1.2 on 2018-12-08 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Truck', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='routes',
            name='price',
            field=models.IntegerField(default=4000),
            preserve_default=False,
        ),
    ]
