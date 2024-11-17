from django.contrib import admin
from .models import Client, Project

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_name', 'created_by', 'created_at', 'updated_at')
    search_fields = ('client_name', 'created_by__username')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'client', 'created_by', 'created_at')
    search_fields = ('project_name', 'client__client_name', 'created_by__username')
    list_filter = ('created_at', 'client')
    ordering = ('-created_at',)
