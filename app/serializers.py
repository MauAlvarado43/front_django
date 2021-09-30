"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

def get_project_serializer():
    import seed.serializers.project as SeedSerializer
    return SeedSerializer.ProjectSerializer

def get_task_serializer():
    import seed.serializers.task as SeedSerializer
    return SeedSerializer.TaskSerializer

def get_user_serializer():
    import seed.serializers.user as SeedSerializer
    return SeedSerializer.UserSerializer

def get_file_serializer():
    import seed.serializers.file as SeedSerializer
    return SeedSerializer.FileSerializer

ProjectSerializer = get_project_serializer()
TaskSerializer = get_task_serializer()
UserSerializer = get_user_serializer()
FileSerializer = get_file_serializer()