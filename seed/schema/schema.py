"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene

import seed.schema.types
import seed.mutations.project
import seed.mutations.task
import seed.mutations.user

class Query(seed.schema.types.Query, graphene.ObjectType):
    pass

class Mutation(graphene.ObjectType):
    saveProject = seed.mutations.project \
        .SaveProjectMutation.Field()
    setProject = seed.mutations.project \
        .SetProjectMutation.Field()
    deleteProject = seed.mutations.project \
        .DeleteProjectMutation.Field()
    saveTask = seed.mutations.task \
        .SaveTaskMutation.Field()
    setTask = seed.mutations.task \
        .SetTaskMutation.Field()
    deleteTask = seed.mutations.task \
        .DeleteTaskMutation.Field()
    saveUser = seed.mutations.user \
        .SaveUserMutation.Field()
    setUser = seed.mutations.user \
        .SetUserMutation.Field()
    deleteUser = seed.mutations.user \
        .DeleteUserMutation.Field()
    pass
schema = graphene.Schema(query=Query, mutation=Mutation)