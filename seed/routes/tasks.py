"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from seed.routes.viewset import ViewSet

from app.models import Task
from app.serializers import TaskSerializer

class TaskViewSet(
    ViewSet,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    def get_queryset(self):
        user = self.request.user
        return Task.filter_permissions(
            super().get_queryset(), Task.permission_filters(user))