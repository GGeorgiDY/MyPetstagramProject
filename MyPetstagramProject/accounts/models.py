from enum import Enum
from django.contrib.auth import models as auth_models
from django.core import validators
from django.db import models
from MyPetstagramProject.core.validators import validate_only_letters


class ChoicesEnumMixin:
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]

    # правим си динамично максималната дължина на gender да е 9 - понеже DoNotShow е най-дългия стринг и е с 9 букви
    @classmethod
    def max_len(cls):
        return max(len(name) for name, _ in cls.choices())


# Enum наследява EnumMeta, която ни дава възможност ние да итерираме. Това означава че ние самия клас може да го пускаме във for цикъл
class Gender(ChoicesEnumMixin, Enum):
    male = 'Male'
    female = 'Female'
    DoNotShow = 'Do not show'


# print(Gender.choices())
# [('male', 'Male'), ('female', 'Female'), ('DoNotShow', 'Do not show')]
# [('male', 'Male'), ('female', 'Female'), ('DoNotShow', 'Do not show')]


class AppUser(auth_models.AbstractUser):
    MIN_LENGTH_FIRST_NAME = 2
    MAX_LENGTH_FIRST_NAME = 30
    MIN_LENGTH_LAST_NAME = 2
    MAX_LENGTH_LAST_NAME = 30

    first_name = models.CharField(
        max_length=MAX_LENGTH_FIRST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LENGTH_FIRST_NAME),
            validate_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=MAX_LENGTH_LAST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LENGTH_LAST_NAME),
            validate_only_letters,
        )
    )

    email = models.EmailField(
        unique=True,
    )

    gender = models.CharField(
        choices=Gender.choices(),
        max_length=Gender.max_len(),
    )

    # ако искам да се логвам с email трябва да напиша
    # USERNAME_FIELD = 'email'
