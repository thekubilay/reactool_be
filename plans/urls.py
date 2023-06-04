from django.urls import path
from plans.views import PlanListAPIView

urlpatterns = [
	path('<int:project_id>/maps/', PlanListAPIView.as_view(), name='map_list'),
]
