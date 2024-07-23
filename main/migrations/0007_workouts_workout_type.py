# Generated by Django 5.0.3 on 2024-06-20 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0006_alter_workouts_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="workouts",
            name="workout_type",
            field=models.CharField(
                choices=[("gain", "gain"), ("lose", "lose")],
                default="gain",
                max_length=50,
            ),
        ),
    ]
