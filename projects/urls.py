from django.urls import path
from projects.views import ProjectRetrieveView, ProjectGroupRetrieveView

urlpatterns = [
	path('project_groups/<int:pk>/', ProjectGroupRetrieveView.as_view(), name='project_group_retrieve'),
	path('projects/<int:pk>/', ProjectRetrieveView.as_view(), name='project_retrieve'),
]
