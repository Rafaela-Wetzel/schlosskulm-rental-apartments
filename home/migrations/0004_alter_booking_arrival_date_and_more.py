# Generated by Django 4.2.13 on 2024-07-02 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_booking_address_alter_booking_amount_guests_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='arrival_date',
            field=models.DateField(help_text="Please enter data in the\n                                    format '2006-10-25'"),
        ),
        migrations.AlterField(
            model_name='booking',
            name='departure_date',
            field=models.DateField(help_text="Please enter data in the\n                                    format '2006-10-25'"),
        ),
    ]
