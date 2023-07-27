from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

UserModel = get_user_model()


class Photos(models.Model):
    class Meta:
        verbose_name_plural = "Photos"

    name = models.CharField(
        max_length=50,
        blank=False,
        null=False,
    )
    about = models.TextField(
        max_length=780,
        null=False,
        blank=False
    )
    url = models.URLField(
        max_length=1000,
        null=False,
        blank=False
    )
    published = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.name}'
