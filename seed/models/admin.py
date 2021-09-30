"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from django.contrib import admin
from djangoql.admin import DjangoQLSearchMixin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from app.models import Project
from app.models import Task
from app.models import User
from app.models import File

class Admin:
    # pylint: disable=R0914,R0915
    @staticmethod
    def register():
        
        class ProjectResource(DjangoQLSearchMixin, resources.ModelResource):
            class Meta:
                model = Project
                fields = (
                    'id',
                    'created_at',
                    'name',
                    'members_id',
                )

        class ProjectAdmin(ImportExportModelAdmin):
            resource_class = ProjectResource
        
        class TaskResource(DjangoQLSearchMixin, resources.ModelResource):
            class Meta:
                model = Task
                fields = (
                    'id',
                    'created_at',
                    'name',
                    'deadline',
                    'status',
                    'assigned_id',
                    'project_id',
                )

        class TaskAdmin(ImportExportModelAdmin):
            resource_class = TaskResource
        
        class UserResource(DjangoQLSearchMixin, resources.ModelResource):
            class Meta:
                model = User
                fields = (
                    'id',
                    'created_at',
                    'username',
                    'first_name',
                    'last_name',
                    'email',
                    'is_active',
                    'photo',
                    'photo_id',
                )

        class UserAdmin(ImportExportModelAdmin):
            resource_class = UserResource
        
        class FileResource(DjangoQLSearchMixin, resources.ModelResource):
            class Meta:
                model = File
        class FileAdmin(ImportExportModelAdmin):
            resource_class = FileResource
        admin.site.register(Project, ProjectAdmin)
        admin.site.register(Task, TaskAdmin)
        admin.site.register(User, UserAdmin)
        admin.site.register(File, FileAdmin)