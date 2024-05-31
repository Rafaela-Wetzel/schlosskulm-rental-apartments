# Generated by Django 4.2.13 on 2024-05-31 13:14

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_alter_booking_departure_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='departure_date',
            field=models.DateField(help_text="Please enter data in the format '2006-10-25'", validators=[]),
        ),
    ]
