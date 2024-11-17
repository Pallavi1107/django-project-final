from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Client, Project

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class ProjectSerializer(serializers.ModelSerializer):
    # users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'project_name','created_at', 'created_by']

class ProjectSerializerId(serializers.ModelSerializer):
    # users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'project_name']

class ClientSerializerId(serializers.ModelSerializer):
    projects = ProjectSerializerId(many=True, read_only=True)
    created_by = serializers.StringRelatedField()

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'projects', 'created_at', 'created_by', 'updated_at']

class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'created_by']
