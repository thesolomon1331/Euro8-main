# Generated by Django 5.0.1 on 2024-01-09 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_rates_dayrate_rates_nightrate'),
    ]

    operations = [
        migrations.AddField(
            model_name='rates',
            name='airport_name',
            field=models.CharField(blank=True, default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='rates',
            name='city_name',
            field=models.CharField(default=None, max_length=30),
        ),
    ]
