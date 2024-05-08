from rest_framework import serializers
from schedulerCrud.models import ScheduleEvents

class ScheduleEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleEvents
        fields = '__all__'