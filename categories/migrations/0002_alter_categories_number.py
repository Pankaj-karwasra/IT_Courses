# Generated by Django 4.1.5 on 2023-10-21 16:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("categories", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="categories",
            name="number",
            field=models.IntegerField(),
        ),
    ]