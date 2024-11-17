from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer,ClientSerializerId,ClientSerializerUpdate,ProjectSerializerId
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ClientDetailViewid(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializerId
    lookup_field = 'id'

class ProjectCreateView(generics.CreateAPIView):
    serializer_class = ProjectSerializerId

    def perform_create(self, serializer):
        client = get_object_or_404(Client, id=self.kwargs['id'])
        created_by = self.request.user
        project = serializer.save(client=client, created_by=created_by)
        users = self.request.data.get('users', [])
        if users:
            project.users.set(users)

class UserProjectsView(generics.ListAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.all()

class ClientDestroyView(generics.DestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'id'

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ClientUpdateView(generics.UpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializerUpdate
    lookup_field = 'id'

