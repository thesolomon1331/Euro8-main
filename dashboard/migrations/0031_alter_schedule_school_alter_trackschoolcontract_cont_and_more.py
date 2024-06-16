# Generated by Django 5.0.2 on 2024-06-09 12:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0030_alter_schedule_drop_time_alter_schedule_pick_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.schoolcontract'),
        ),
        migrations.AlterField(
            model_name='trackschoolcontract',
            name='cont',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.schoolcontract'),
        ),
        migrations.AlterField(
            model_name='trackschoolcontract',
            name='contract',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.schedule'),
        ),
    ]