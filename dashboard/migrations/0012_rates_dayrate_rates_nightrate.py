# Generated by Django 5.0.1 on 2024-01-09 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_rates'),
    ]

    operations = [
        migrations.AddField(
            model_name='rates',
            name='dayRate',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='rates',
            name='nightRate',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]