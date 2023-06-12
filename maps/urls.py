from django.urls import path
from maps.views import MapListAPIView

urlpatterns = [
	path('<int:project_id>/maps/', MapListAPIView.as_view(), name='maps_list'),
	path('<int:project_id>/map_categories/', MapListAPIView.as_view(), name='map_categories_list'),
]
