from django.contrib.auth import get_user_model
from django.db import models
from quitter.quits.models import Quit


UserModel = get_user_model()


class Like(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
    for_quit = models.ForeignKey(
        Quit,
        on_delete=models.CASCADE
    )


class Comment(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
    for_quit = models.ForeignKey(
        Quit,
        on_delete=models.CASCADE
    )
    comment_text = models.TextField(
        max_length=780,
        blank=False,
        null=False,
    )
    published = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True
    )


class Follow(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
    for_user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='follow_user'
    )
