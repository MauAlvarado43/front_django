"""
__Seed builder__
  Extended module
"""

import seed.routes.tasks as SeedRoute
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from seed.util.request_util import has_fields_or_400
from app.models import Task
from app.serializers import TaskSerializer

class TaskViewSet(SeedRoute.TaskViewSet):
  
  """ GET /api/tasks/timeline """
  @action(detail=False, methods=["GET"])
  def timeline(self, request):

    return Response({
      "jan": 15,
      "feb": 12,
      "mar": 19,
      "abr": 4,
      "may": 20,
      "jun": 8
    })
