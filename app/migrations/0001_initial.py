# Generated by Django 4.2 on 2023-04-28 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="restaurant",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=10)),
                ("category", models.CharField(max_length=10)),
                ("location_long", models.FloatField()),
                ("location_lat", models.FloatField()),
            ],
            options={
                "db_table": "restaurant",
            },
        ),
        migrations.CreateModel(
            name="User",
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
                ("email", models.CharField(max_length=20)),
                ("name", models.CharField(max_length=20)),
                ("pwd", models.CharField(max_length=20)),
            ],
        ),
    ]
