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
    connections = models.ManyToManyField("self", through='UserConnection', symmetrical=False)

    def __unicode__(self):
        return self.username


class UserGroup(models.Model):
    """
    a user can make a group with some name and description.
    """
    name = models.CharField(max_length=50)
    description = models.TextField()
    owner = models.ForeignKey(User)

    def __unicode__(self):
        return self.name


class UserConnection(models.Model):
    """
    through table of User, field_name:-connections
    users can add other users in there network
    """
    source = models.ForeignKey(User, related_name='source')
    target = models.ForeignKey(User, related_name='target')
    group = models.ForeignKey(UserGroup)

    def __unicode__(self):
        return self.source