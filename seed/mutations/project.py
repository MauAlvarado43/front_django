"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from app.models import Project
from app.models import User
from seed.schema.types import Project as ProjectType

class SaveProjectMutation(graphene.Mutation):
    
    project = graphene.Field(ProjectType)
    
    class Arguments:
        name = graphene.String(required=True)
        members = graphene.Int(required=True)
        pass
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        project = {}
        if "name" in kwargs:
            project["name"] = kwargs["name"]
        if "members" in kwargs:
            members = User.filter_permissions(
                User.objects,
                User.permission_filters(user)) \
                .get(pk=kwargs["members"])
            project["members"] = members
        project = \
            Project.objects.create(**project)
        project.save()
    
        return SaveProjectMutation(
            project=project)

class SetProjectMutation(graphene.Mutation):
    
    project = graphene.Field(ProjectType)
    
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=False)
        members = graphene.Int(required=False)
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        project = Project.filter_permissions(
            Project.objects,
            Project.permission_filters(user)) \
            .get(pk=kwargs["id"])
        if "name" in kwargs:
            project.name = kwargs["name"]
        if "members" in kwargs:
            members = User.objects \
                .get(pk=kwargs["members"])
            project.members = members
        project.save()
    
        return SetProjectMutation(
            project=project)

class DeleteProjectMutation(graphene.Mutation):
    
    id = graphene.Int()
    
    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        project_id = kwargs["id"]
        project = Project.objects.get(pk=kwargs["id"])
        project.delete()
        return DeleteProjectMutation(
            id=project_id)