"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from app.models import User
from app.models import File
from seed.schema.types import User as UserType

class SaveUserMutation(graphene.Mutation):
    
    user = graphene.Field(UserType)
    
    class Arguments:
        username = graphene.String(required=True)
        firstName = graphene.String(required=True)
        lastName = graphene.String(required=True)
        email = graphene.String(required=True)
        isActive = graphene.Boolean(required=True)
        password = graphene.String(required=True)
        photo = graphene.Int(required=True)
        pass
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        user = {}
        if "userName" in kwargs:
            user["user_name"] = kwargs["userName"]
        if "firstName" in kwargs:
            user["first_name"] = kwargs["firstName"]
        if "lastName" in kwargs:
            user["last_name"] = kwargs["lastName"]
        if "email" in kwargs:
            user["email"] = kwargs["email"]
        if "isActive" in kwargs:
            user["is_active"] = kwargs["isActive"]
        if "photo" in kwargs:
            photo = File.filter_permissions(
                File.objects,
                File.permission_filters(user)) \
                .get(pk=kwargs["photo"])
            user["photo"] = photo
        user = \
            User.objects.create(**user)
        if "password" in kwargs: user.set_password(kwargs["password"])
        user.save()
    
        return SaveUserMutation(
            user=user)

class SetUserMutation(graphene.Mutation):
    
    user = graphene.Field(UserType)
    
    class Arguments:
        id = graphene.Int(required=True)
        username = graphene.String(required=False)
        firstName = graphene.String(required=False)
        lastName = graphene.String(required=False)
        email = graphene.String(required=False)
        isActive = graphene.Boolean(required=False)
        password = graphene.String(required=False)
        photo = graphene.Int(required=False)
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        user = User.filter_permissions(
            User.objects,
            User.permission_filters(user)) \
            .get(pk=kwargs["id"])
        if "userName" in kwargs:
            user.user_name = kwargs["userName"]
        if "firstName" in kwargs:
            user.first_name = kwargs["firstName"]
        if "lastName" in kwargs:
            user.last_name = kwargs["lastName"]
        if "email" in kwargs:
            user.email = kwargs["email"]
        if "isActive" in kwargs:
            user.is_active = kwargs["isActive"]
        if "password" in kwargs:
            user.set_password(kwargs["password"])
        if "photo" in kwargs:
            photo = File.objects \
                .get(pk=kwargs["photo"])
            user.photo = photo
        user.save()
    
        return SetUserMutation(
            user=user)

class DeleteUserMutation(graphene.Mutation):
    
    id = graphene.Int()
    
    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        user_id = kwargs["id"]
        user = User.objects.get(pk=kwargs["id"])
        user.delete()
        return DeleteUserMutation(
            id=user_id)