from django.core.validators import MinLengthValidator
from django.db import models
from datetime import date
from . import validators as validators
from django.contrib.auth import models as auth_models
# Create your models here.


class QuitterUser(auth_models.AbstractUser):
    first_name = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(3),
            validators.only_letters,
            validators.starts_with_capital_letter,
        ],
    )
    last_name = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(3),
            validators.only_letters,
            validators.starts_with_capital_letter,
        ],
    )
    email = models.EmailField(
        unique=False,
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True,
        default=date(2000, 1, 1)
    )
    gender = models.CharField(
        choices=validators.Gender.choices(),
        max_length=50,
        default=validators.Gender.do_not_show,
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
        default='https://icon-library.com/images/no-user-image-icon/no-user-image-icon-0.jpg'
    )
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.username
