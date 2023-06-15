from plans.models import RoomPlan, GeneralPlan
from rest_framework import serializers


class RoomPlanSerializer(serializers.ModelSerializer):
	class Meta:
		model = RoomPlan
		fields = '__all__'


class GeneralPlanSerializer(serializers.ModelSerializer):
	class Meta:
		model = GeneralPlan
		fields = '__all__'
