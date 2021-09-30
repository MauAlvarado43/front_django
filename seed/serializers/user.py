"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from app.models import User
from app.models import File
from seed.serializers.file import FileSerializer

class UserSerializer(serializers.ModelSerializer):
    
    photo = FileSerializer(read_only=True)

    photo_id = serializers.PrimaryKeyRelatedField(
        source='photo', queryset=File.objects.all(),
        required=True, allow_null=False)

    class Meta:
        model = User
        fields = (
            'id',
            'hash',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_active',
            'photo',
            'photo_id',  
        )