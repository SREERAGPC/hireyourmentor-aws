# Generated by Django 4.0.4 on 2022-06-03 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('slots', '0001_initial'),
        ('booking', '0002_alter_booking_details_booked_slot_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking_details',
            name='booked_slot',
        ),
        migrations.AddField(
            model_name='booking_details',
            name='slot',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='slots.slots'),
        ),
    ]
