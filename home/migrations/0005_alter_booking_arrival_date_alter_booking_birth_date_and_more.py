# Generated by Django 4.2.13 on 2024-07-04 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_booking_arrival_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='arrival_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='birth_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='departure_date',
            field=models.DateField(),
        ),
    ]
