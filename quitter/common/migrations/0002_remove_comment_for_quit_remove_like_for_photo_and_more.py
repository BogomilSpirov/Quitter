# Generated by Django 4.2.3 on 2023-07-18 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("quits", "0004_alter_quit_tagged_people"),
        ("common", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="for_quit",
        ),
        migrations.RemoveField(
            model_name="like",
            name="for_photo",
        ),
        migrations.AddField(
            model_name="comment",
            name="quit",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="quits.quit"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="like",
            name="quit",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="quits.quit"
            ),
            preserve_default=False,
        ),
    ]
