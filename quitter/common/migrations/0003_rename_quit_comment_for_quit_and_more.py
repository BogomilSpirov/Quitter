# Generated by Django 4.2.3 on 2023-07-18 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0002_remove_comment_for_quit_remove_like_for_photo_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="quit",
            new_name="for_quit",
        ),
        migrations.RenameField(
            model_name="like",
            old_name="quit",
            new_name="for_quit",
        ),
    ]
