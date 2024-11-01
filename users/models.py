from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

  class GenderChoices(models.TextChoices):
    MALE = ("male", "Male")  # ("value to database", "label for admin panel")
    FEMALE = ("female", "Female")

  class LanguageChoices(models.TextChoices):
    KR = ("kr", "Korean")
    EN = ("en", "English")

  # AbstractUser first_name, last_name overriding
  first_name = models.CharField(
      max_length=150,
      editable=False,
  )  # editable=False -> user cannot use
  last_name = models.CharField(
      max_length=150,
      editable=False,
  )
  avatar = models.ImageField(blank=True)
  name = models.CharField(
      max_length=150,
      default="",
  )
  gender = models.CharField(
      max_length=10,
      choices=GenderChoices.choices,
      default="",
  )
  lanaguage = models.CharField(
      max_length=2,
      choices=LanguageChoices.choices,
      default="",
  )

  def __str__(self):
    return self.username
