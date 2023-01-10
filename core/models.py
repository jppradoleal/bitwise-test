from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser, PermissionsMixin


# Create your models here.
class User(AbstractUser, PermissionsMixin):
    USERNAME_FIELD = "email"


class Gender(models.TextChoices):
    MALE = "MALE", _("Male")
    FEMALE = "FEMALE", _("Female")
    NOT_SPECIFIED = "NOT_SPECIFIED", _("Not Specified")


class GithubProfile(models.Model):
    username = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    profile_image_url = models.URLField(null=True)
    bio = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    gender = models.TextChoices(null=True)
    followers = models.IntegerField()
    following = models.IntegerField()
    hireable = models.BooleanField()
    blog = models.URLField(null=True)
    company = models.CharField(max_length=30, null=True)
