# Generated by Django 3.2.25 on 2024-04-12 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_auto_20240412_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='allergies',
            field=models.CharField(default='No Allergies Stated', max_length=150),
        ),
    ]
