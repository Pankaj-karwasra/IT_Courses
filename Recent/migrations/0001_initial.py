# Generated by Django 4.1.5 on 2023-10-21 16:49

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Recent",
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
                ("image", models.ImageField(upload_to="detail/")),
                ("title", models.CharField(max_length=250)),
                ("name", models.CharField(max_length=250)),
                ("rating", models.IntegerField()),
                ("number", models.IntegerField()),
            ],
        ),
    ]
