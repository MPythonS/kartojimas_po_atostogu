from django.contrib import admin

from portfolio_app.models import Project


# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'project_resume',
        'utl',
        'utl1',
        'utl2',
        'utl3',
        'utl4',
        'utl5',
        'utl6',
        'utl7',
        'project_start_date',
        'project_status',
        'c_remarks',
        'c_created_at',
        'c_updated_at')
    list_filter = ()


admin.site.register(Project, ProjectAdmin)