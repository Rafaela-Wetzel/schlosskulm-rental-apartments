# Generated by Django 4.2.13 on 2024-05-27 14:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['last_name', 'first_name']},
        ),
        migrations.AlterField(
            model_name='booking',
            name='phone_number',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='user_name', to=settings.AUTH_USER_MODEL),
        ),
    ]