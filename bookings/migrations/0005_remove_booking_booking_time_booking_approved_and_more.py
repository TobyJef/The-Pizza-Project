# Generated by Django 5.0.4 on 2024-05-05 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_alter_booking_dietary_requirements'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='booking_time',
        ),
        migrations.AddField(
            model_name='booking',
            name='approved',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='end_time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='start_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_size',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
