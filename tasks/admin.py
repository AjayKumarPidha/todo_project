from django.contrib import admin
from tasks.models import Task  # import Task model


# Task Admin
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "status", "user", "due_date", "created_at")
    list_filter = ("status", "due_date")
    search_fields = ("title", "description", "user__email")
    ordering = ("-created_at",)

admin.site.register(Task, TaskAdmin)
