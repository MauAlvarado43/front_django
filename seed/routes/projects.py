"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from seed.routes.viewset import ViewSet

from app.models import Project
from app.serializers import ProjectSerializer

class ProjectViewSet(
    ViewSet,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    def get_queryset(self):
        user = self.request.user
        return Project.filter_permissions(
            super().get_queryset(), Project.permission_filters(user))