# Generated by Django 5.0 on 2023-12-24 10:49

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_complaintform_complintid_driverfiles'),
    ]

    operations = [
        migrations.AddField(
            model_name='driverfiles',
            name='accept_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='driverfiles',
            name='all_files_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='driverfiles',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='complaintform',
            name='ComplintId',
            field=models.CharField(default='CM56217430', max_length=10, null=True),
        ),
    ]
