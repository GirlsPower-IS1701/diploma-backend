from rest_framework import serializers

from accounts.serializers import UserSerializer
from .models import Timetable


class TimetableSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = Timetable
        fields = ('id', 'day_of_week', 'lesson_type', 'start_time', 'finish_time', 'room_number')