# Generated by Django 4.2.3 on 2023-07-18 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0005_quitteruser_date_of_birth"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="quitteruser",
            name="age",
        ),
    ]