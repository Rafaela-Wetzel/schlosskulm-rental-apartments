# Generated by Django 4.2.13 on 2024-05-31 13:07

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_alter_booking_address_alter_booking_amount_guests_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='arrival_date',
            field=models.DateField(help_text="Please enter data in the format '2006-10-25'", validators=[]),
        ),
        migrations.AlterField(
            model_name='booking',
            name='birth_date',
            field=models.DateField(help_text="Please enter data in the format '2006-10-25'", validators=[]),
        ),
        migrations.AlterField(
            model_name='booking',
            name='departure_date',
            field=models.DateField(help_text="Please enter data in the format '2006-10-25'", validators=[]),
        ),
    ]