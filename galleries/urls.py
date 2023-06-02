from django.urls import path
from galleries.views import GalleryListAPIView

urlpatterns = [
	path('<int:project_id>/galleries/', GalleryListAPIView.as_view(), name='gallery_list'),
]
