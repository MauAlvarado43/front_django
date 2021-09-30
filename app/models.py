"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

def get_project():
    import seed.models.project as SeedModel
    return SeedModel.Project

def get_task():
    import seed.models.task as SeedModel
    return SeedModel.Task

def get_user():
    import seed.models.user as SeedModel
    return SeedModel.User

def get_file():
    import seed.models.file as SeedFile
    return SeedFile.File

Project = get_project()
Task = get_task()
User = get_user()
File = get_file()