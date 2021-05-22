from rest_framework import serializers

from accounts.serializers import UserSerializer
from .models import Timetable

from speciality_groups.serializers EnrollmentSerializer

class TimetableSerialaizer(serializers.ModelSerializer):
    enrollment = EnrollmentSerializer(read_only=True)
    class Meta:
        model = Timetable
        fields = ('id', 'day_of_week', 'lesson_type', 'enrollment', 'start_time', 'finish_time', 'room_number')