from django.urls import path
from projects.views import ProjectRetrieveView

urlpatterns = [
	path('projects/<int:pk>/', ProjectRetrieveView.as_view(), name='project_retrieve'),
]
