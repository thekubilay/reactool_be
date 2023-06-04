from django.urls import path
from maps.views import MapListAPIView

urlpatterns = [
	path('<int:project_id>/maps/', MapListAPIView.as_view(), name='map_list'),
]
