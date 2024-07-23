# Generated by Django 5.0.3 on 2024-06-20 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_measurement"),
    ]

    operations = [
        migrations.CreateModel(
            name="Workouts",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="")),
            ],
        ),
    ]
