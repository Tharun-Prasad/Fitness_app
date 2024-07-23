# Generated by Django 5.0.3 on 2024-06-21 04:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0015_alter_workoutplans_days"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprogress",
            name="plan",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="main.workoutplans"
            ),
        ),
        migrations.AddConstraint(
            model_name="workoutplans",
            constraint=models.UniqueConstraint(
                fields=("title", "days"), name="unique_title_days"
            ),
        ),
    ]
