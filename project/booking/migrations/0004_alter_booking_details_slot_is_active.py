# Generated by Django 4.0.4 on 2022-06-03 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_remove_booking_details_booked_slot_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking_details',
            name='slot_is_active',
            field=models.BooleanField(default=True),
        ),
    ]
