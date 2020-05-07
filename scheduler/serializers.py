from rest_framework import serializers
from scheduler.models import Schedule

class ScheduleSerializer(serializers.ModelSerializer):
  class Meta:
    model = Schedule
    fields = '__all__'
