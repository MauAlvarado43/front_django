"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from app.models import Task
from app.models import User
from app.models import Project
from seed.schema.types import Task as TaskType

class SaveTaskMutation(graphene.Mutation):
    
    task = graphene.Field(TaskType)
    
    class Arguments:
        name = graphene.String(required=True)
        deadline = graphene.DateTime(required=True)
        status = graphene.String(required=True)
        assigned = graphene.Int(required=True)
        project = graphene.Int(required=True)
        pass
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        task = {}
        if "name" in kwargs:
            task["name"] = kwargs["name"]
        if "deadline" in kwargs:
            task["deadline"] = kwargs["deadline"]
        if "status" in kwargs:
            task["status"] = kwargs["status"]
        if "assigned" in kwargs:
            assigned = User.filter_permissions(
                User.objects,
                User.permission_filters(user)) \
                .get(pk=kwargs["assigned"])
            task["assigned"] = assigned
        if "project" in kwargs:
            project = Project.filter_permissions(
                Project.objects,
                Project.permission_filters(user)) \
                .get(pk=kwargs["project"])
            task["project"] = project
        task = \
            Task.objects.create(**task)
        task.save()
    
        return SaveTaskMutation(
            task=task)

class SetTaskMutation(graphene.Mutation):
    
    task = graphene.Field(TaskType)
    
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=False)
        deadline = graphene.DateTime(required=False)
        status = graphene.String(required=False)
        assigned = graphene.Int(required=False)
        project = graphene.Int(required=False)
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        task = Task.filter_permissions(
            Task.objects,
            Task.permission_filters(user)) \
            .get(pk=kwargs["id"])
        if "name" in kwargs:
            task.name = kwargs["name"]
        if "deadline" in kwargs:
            task.deadline = kwargs["deadline"]
        if "status" in kwargs:
            task.status = kwargs["status"]
        if "assigned" in kwargs:
            assigned = User.objects \
                .get(pk=kwargs["assigned"])
            task.assigned = assigned
        if "project" in kwargs:
            project = Project.objects \
                .get(pk=kwargs["project"])
            task.project = project
        task.save()
    
        return SetTaskMutation(
            task=task)

class DeleteTaskMutation(graphene.Mutation):
    
    id = graphene.Int()
    
    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        task_id = kwargs["id"]
        task = Task.objects.get(pk=kwargs["id"])
        task.delete()
        return DeleteTaskMutation(
            id=task_id)