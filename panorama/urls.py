from django.urls import path
from panorama.views import PanoramaListAPIView

urlpatterns = [
	path('<int:project_id>/panorama/', PanoramaListAPIView.as_view(), name='panorama_list'),
]
