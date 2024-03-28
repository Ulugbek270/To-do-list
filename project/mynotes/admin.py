from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'complete', 'created_at']
    list_filter = ['complete']


admin.site.register(Task, TaskAdmin)
