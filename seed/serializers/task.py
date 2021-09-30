"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from app.models import Task
from app.models import User
from app.models import Project

class TaskSerializer(serializers.ModelSerializer):

    assigned_id = serializers.PrimaryKeyRelatedField(
        source='assigned', queryset=User.objects.all(),
        required=True, allow_null=False)
    project_id = serializers.PrimaryKeyRelatedField(
        source='project', queryset=Project.objects.all(),
        required=True, allow_null=False)

    class Meta:
        model = Task
        fields = (
            'id',
            'hash',
            'name',
            'deadline',
            'status',
            'assigned_id',
            'project_id',  
        )