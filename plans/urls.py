from django.urls import path
from plans.views import RoomPlanListAPIView, GeneralPlanListAPIView

urlpatterns = [
	path('<int:project_id>/room_plans/', RoomPlanListAPIView.as_view(), name='room_plan_list'),
	path('<int:project_id>/general_plans/', GeneralPlanListAPIView.as_view(), name='general_plan_list'),
]
