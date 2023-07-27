from enum import Enum
from django.core.exceptions import ValidationError


def only_letters(value):
    if not value.isalpha():
        raise ValidationError(f'Only letters are allowed for {value}.')


def starts_with_capital_letter(value):
    if not value[0].isupper():
        raise ValidationError('Name must start with capital letter.')


class Gender(Enum):
    @classmethod
    def choices(cls):
        return [(choice.value, choice.name) for choice in cls]

    @classmethod
    def max_len(cls):
        return max(len(choice.value) for choice in cls)

    male = 'male'
    female = 'female'
    do_not_show = 'do_not_show'


