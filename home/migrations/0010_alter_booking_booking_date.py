# Generated by Django 4.2.13 on 2024-05-30 12:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_booking_booking_date_alter_booking_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]