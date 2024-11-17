from django.urls import path
from .views import ClientListCreateView, ClientDetailViewid, ProjectCreateView, UserProjectsView,ClientDestroyView,ClientUpdateView

urlpatterns = [
    path('clients/', ClientListCreateView.as_view(), name='client-list-create'),
    path('clients/<int:id>/', ClientDetailViewid.as_view(), name='client-detail'),
    path('clients/<int:id>/projects/', ProjectCreateView.as_view(), name='project-create'),
    path('projects/', UserProjectsView.as_view(), name='user-projects'),
    path('clients/<int:id>/', ClientDestroyView.as_view(), name='client-delete'),
    path('clients/<int:id>/', ClientUpdateView.as_view(), name='client-update'),
]
