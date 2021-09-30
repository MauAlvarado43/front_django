"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from django.db import models
from seed.models.model import Model

class Project(Model):

    name = models.CharField(max_length=255, blank=True)

    members = models.ForeignKey(
        'models.User', related_name='members_projects',
        blank=False, null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = '_project'
        app_label = 'models'