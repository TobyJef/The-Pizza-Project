# Generated by Django 3.2.25 on 2024-04-30 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booking_size',
            field=models.IntegerField(null=True),
        ),
    ]
