# Generated by Django 5.0.3 on 2024-06-21 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0013_alter_workoutplans_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="workoutplans",
            name="days",
            field=models.IntegerField(
                choices=[(15, 15), (30, 30)], default=15, max_length=50
            ),
        ),
    ]
