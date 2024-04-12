# Generated by Django 3.2.25 on 2024-04-12 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_alter_booking_allergies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='address',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateField(max_length=8),
        ),
        migrations.AlterField(
            model_name='booking',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
