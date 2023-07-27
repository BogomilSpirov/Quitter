# Generated by Django 4.2.3 on 2023-07-14 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Photos",
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
                ("name", models.CharField(max_length=50)),
                ("about", models.TextField()),
                ("url", models.URLField()),
                ("published", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
