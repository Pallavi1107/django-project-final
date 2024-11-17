from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer,ClientSerializerId
from django.shortcuts import get_object_or_404

class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ClientDetailViewid(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializerId
    # permission_classes = [IsAuthenticated]
    lookup_field = 'id'

class ProjectCreateView(generics.CreateAPIView):
    serializer_class = ProjectSerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        client = get_object_or_404(Client, id=self.kwargs['id'])  # Corrected here
        serializer.save(client=client, created_by=self.request.user)

class UserProjectsView(generics.ListAPIView):
    serializer_class = ProjectSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.projects.all()
