from django.db import models
from django.contrib.auth.models import AbstractUser
from .choices import STATUS_CHOICES


class User(AbstractUser):
    """
    Extending the base USER model to add more user fields.
    field:status  for status of a user by default pending, chanaged to verified/rejected depends on mail response.
    field:organisation:  for name of organisation
    """
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='Pending')
    organisation = models.CharField(max_length=100)

    def __unicode__(self):
        return self.username


