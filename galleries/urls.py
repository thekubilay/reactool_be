from galleries.views import GalleryRetrieveAPIView
from django.urls import path

urlpatterns = [
	path('galleries/<int:pk>/', GalleryRetrieveAPIView.as_view()),
]
