from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.core.validators import MinValueValidator, MaxValueValidator


class CustomUser(AbstractUser):
    pass

