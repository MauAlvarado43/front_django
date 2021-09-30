"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from datetime import datetime
from django.db import models
from seed.models.model import Model

class Task(Model):
    
    STATUSES = (
        ('TODO', 'TODO'),
        ('IN_PROCESS', 'IN_PROCESS'),
        ('COMPLETED', 'COMPLETED'),
    )

    name = models.CharField(max_length=255, blank=True)
    deadline = models.DateTimeField(
        blank=False, null=False, default=datetime.now)
    status = models.CharField(
        max_length=64, choices=STATUSES,
        blank=False)

    assigned = models.ForeignKey(
        'models.User', related_name='assigned_tasks',
        blank=False, null=False, on_delete=models.CASCADE)
    project = models.ForeignKey(
        'models.Project', related_name='tasks',
        blank=False, null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = '_task'
        app_label = 'models'