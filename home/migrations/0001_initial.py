# Generated by Django 4.2.13 on 2024-06-03 16:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('booking_status', models.CharField(blank=True, choices=[('Requested', 'Requested'), ('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled')], default='Requested', null=True)),
                ('first_name', models.CharField(default='Henna', max_length=100)),
                ('last_name', models.CharField(default='Hamma', max_length=100)),
                ('birth_date', models.DateField(default='2006-10-25', help_text="Please enter data in the format '2006-10-25'")),
                ('email', models.EmailField(default='hello@gmx.de', max_length=100)),
                ('phone_number', models.BigIntegerField(default='123')),
                ('address', models.CharField(default='Hello street 6', max_length=200)),
                ('zip_code', models.CharField(default='12345', max_length=100)),
                ('city', models.CharField(default='Monster City', max_length=100)),
                ('country', models.CharField(default='Monster Country', max_length=100)),
                ('booking_item', models.CharField(choices=[('Upper Apartment', 'Upper Apartment'), ('Lower Apartment', 'Lower Apartment'), ('Whole House', 'Whole House')], default='Upper Apartment')),
                ('arrival_date', models.DateField(default='2024-10-30', help_text="Please enter data in the format '2006-10-25'")),
                ('departure_date', models.DateField(default='2024-10-31', help_text="Please enter data in the format '2006-10-25'")),
                ('amount_guests', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15')], default='1')),
                ('nationality', models.CharField(choices=[('German', 'German'), ('Other', 'Other')], default='German')),
                ('passport_number', models.CharField(blank=True, default='234', max_length=100, null=True)),
                ('animals', models.BooleanField(blank=True, null=True)),
                ('message', models.TextField(default='Hi!', max_length=1000)),
                ('user', models.ForeignKey(default='1', on_delete=django.db.models.deletion.RESTRICT, related_name='user_name', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
