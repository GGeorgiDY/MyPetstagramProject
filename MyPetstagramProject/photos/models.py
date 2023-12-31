from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from MyPetstagramProject.core.model_mixins import StrFromFieldsMixin
from MyPetstagramProject.pets.models import Pet
from MyPetstagramProject.photos.validators import validate_file_less_than_5mb


UserModel = get_user_model()


class Photo(StrFromFieldsMixin, models.Model):
    str_fields = ('pk', 'photo', 'location')
    MIN_DESCRIPTION_LENGTH = 10
    MAX_DESCRIPTION_LENGTH = 300
    MAX_LOCATION_LENGTH = 30

    # Requires mediafiles to work correctly
    photo = models.ImageField(
        upload_to='pet_photos/',
        null=False,
        blank=True,
        validators=(validate_file_less_than_5mb,),
    )

    description = models.CharField(
        # DB validation
        max_length=MAX_DESCRIPTION_LENGTH,
        # Django/python validation, not DB validation
        validators=(
            MinLengthValidator(MIN_DESCRIPTION_LENGTH),
        ),
        null=True,
        blank=True,
    )

    location = models.CharField(
        max_length=MAX_LOCATION_LENGTH,
        null=True,
        blank=True,
    )

    publication_date = models.DateField(
        # Automatically sets current date on 'save' (update or create)
        auto_now=True,
        null=False,
        blank=True,
    )

    # Many-to-many relation
    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True,
    )

    # One-to-many relations
    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )

