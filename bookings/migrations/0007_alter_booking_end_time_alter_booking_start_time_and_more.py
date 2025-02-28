# Generated by Django 5.0.4 on 2024-05-10 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0006_alter_booking_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='end_time',
            field=models.TimeField(choices=[('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00'), ('16:00', '16:00'), ('17:00', '17:00'), ('18:00', '18:00'), ('19:00', '19:00'), ('20:00', '20:00'), ('21:00', '21:00')], null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_time',
            field=models.TimeField(choices=[('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00'), ('16:00', '16:00'), ('17:00', '17:00'), ('18:00', '18:00'), ('19:00', '19:00'), ('20:00', '20:00'), ('21:00', '21:00')], null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='title',
            field=models.CharField(blank=True, choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Miss', 'Miss'), ('Ms', 'Ms'), ('Dr', 'Dr'), ('Prof', 'Prof'), ("Rev'd", "Rev'd")], max_length=10),
        ),
    ]
