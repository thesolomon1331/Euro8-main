# Generated by Django 5.0.2 on 2024-06-09 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0027_schedule_drop_time_schedule_pick_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='drop_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='pick_time',
            field=models.TimeField(null=True),
        ),
    ]
