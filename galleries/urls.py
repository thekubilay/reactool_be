from django.urls import path
from galleries.views import GalleryListAPIView

urlpatterns = [
	path('galleries/<int:project_id>/', GalleryListAPIView.as_view(), name='gallery_list'),
]
