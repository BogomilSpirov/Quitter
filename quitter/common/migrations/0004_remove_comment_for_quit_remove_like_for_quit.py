# Generated by Django 4.2.3 on 2023-07-18 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0003_rename_quit_comment_for_quit_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="for_quit",
        ),
        migrations.RemoveField(
            model_name="like",
            name="for_quit",
        ),
    ]