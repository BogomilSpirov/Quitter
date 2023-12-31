# Generated by Django 4.2.3 on 2023-07-23 11:22

import django.core.validators
from django.db import migrations, models
import quitter.accounts.validators


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0008_alter_quitteruser_last_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="quitteruser",
            name="last_name",
            field=models.CharField(
                max_length=50,
                validators=[
                    django.core.validators.MinLengthValidator(3),
                    quitter.accounts.validators.only_letters,
                ],
            ),
        ),
    ]
