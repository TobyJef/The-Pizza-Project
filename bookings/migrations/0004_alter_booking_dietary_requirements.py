# Generated by Django 5.0.4 on 2024-05-03 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_rename_additional_requests_booking_requests_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='dietary_requirements',
            field=models.CharField(default='No Diertary Requirements/Allergies Stated', max_length=150),
        ),
    ]
