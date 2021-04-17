from rest_framework import serializers

from accounts.serializers import UserSerializer
from speciality_groups.serializers import EnrollmentSerializer
from .models import Room_Type, Room, Lession_Time, TimeTable

class RoomTypeSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = Room_Type
        fields = ('id', 'title', 'description')


class RoomSerializer(serializers.ModelSerializer):
    room_type = RoomTypeSerialaizer(read_only=True)
    class Meta:
        model = Room
        fields = ('id', 'number', 'room_type')

class LessionTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lession_Time
        fields = ('id', 'number', 'time_begin', 'time_end')


class TimetableSerializer(serializers.ModelSerializer):
    enrollment = EnrollmentSerializer(read_only=True)
    room = RoomSerializer(read_only=True)
    lession_time = LessionTimeSerializer(read_only=True)
    class Meta:
        model = TimeTable
        fields = ('id', 'day', 'enrollment', 'room', 'lession_time')