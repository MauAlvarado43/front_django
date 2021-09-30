"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

def get_project_viewset():
    import seed.routes.projects as SeedViewSet
    return SeedViewSet.ProjectViewSet

def get_task_viewset():
    import routes.tasks as ExtendViewSet
    return ExtendViewSet.TaskViewSet

def get_user_viewset():
    import seed.routes.users as SeedViewSet
    return SeedViewSet.UserViewSet

def get_file_view():
    import seed.routes.files as SeedView
    return SeedView.FileView

ProjectViewSet = get_project_viewset()
TaskViewSet = get_task_viewset()
UserViewSet = get_user_viewset()
FileView = get_file_view()