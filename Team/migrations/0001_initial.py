# Generated by Django 4.1.5 on 2023-10-15 16:04

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Team",
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
                ("image",models.ImageField(upload_to='team/')),
                ("name", models.CharField(max_length=255)),
                ("course", models.CharField(max_length=255)),

            ],
        ),
    ]
