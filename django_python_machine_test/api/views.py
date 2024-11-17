from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer,ClientSerializerId
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
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        client = get_object_or_404(Client, id=self.kwargs['id'])  # Corrected here
        serializer.save(client=client, created_by=self.request.user)

class UserProjectsView(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return self.request.user.projects.all()

class ClientDestroyView(generics.DestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'id'

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)
