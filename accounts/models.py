from django.db import models
from django.contrib.auth.models import AbstractUser

TYPE = (
  ("mentor", "メンター"),
  ("mentee","メンティー"),
  )
class CustomUser(AbstractUser):
  registration_type = models.CharField(max_length=10, choices=TYPE)
  profile = models.TextField(null=True,  blank=True)
