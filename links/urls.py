from django.urls import path
from links.views import LinkListAPIView

urlpatterns = [
	path('<int:project_id>/links/', LinkListAPIView.as_view(), name='link_list'),
]
