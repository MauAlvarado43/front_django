"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from django.contrib.auth.models import AbstractUser
from django.db import models
from seed.models.model import Model

class User(AbstractUser, Model):

    photo = models.ForeignKey(
        'models.File', related_name='user_photos',
        blank=False, null=False, on_delete=models.PROTECT)

    class Meta:
        db_table = '_user'
        app_label = 'models'