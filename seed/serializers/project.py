"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from app.models import Project
from app.models import User

class ProjectSerializer(serializers.ModelSerializer):

    members_id = serializers.PrimaryKeyRelatedField(
        source='members', queryset=User.objects.all(),
        required=True, allow_null=False)

    class Meta:
        model = Project
        fields = (
            'id',
            'hash',
            'name',
            'members_id',  
        )