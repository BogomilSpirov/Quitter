from django.contrib.auth import get_user_model
from django.db import models
from quitter.photos.models import Photos


UserModel = get_user_model()


class Quit(models.Model):
    title = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
    photo = models.ForeignKey(
        Photos,
        on_delete=models.CASCADE
    )
    description = models.TextField(
        null=False,
        blank=False
    )
    tagged_people = models.ManyToManyField(
        UserModel,
        related_name="tagged_people",
        blank=True
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.title}'
