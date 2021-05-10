from rest_framework import serializers

from accounts.serializers import UserSerializer
from .models import Academic_Degree, Academic_Rank, Position_Types, Positions, Staff, StaffProfile


class AcademicDegreeSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = Academic_Degree
        fields = ('id', 'title')


class AcademicRankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Academic_Rank
        fields = ('id', 'description')


class PositionTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position_Types
        fields = ('id', 'description')

class PositionSerializer(serializers.ModelSerializer):
    position_type = PositionTypesSerializer(read_only=True)
    class Meta:
        model = Positions
        fields = ('id', 'position_type', 'description')

class StaffSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    academic_degree = AcademicDegreeSerialaizer(read_only=True)
    academic_rank = AcademicRankSerializer(read_only=True)
    position = PositionSerializer(read_only=True)
    class Meta:
        model = Staff
        fields = ('id', 'user', 'academic_degree', 'academic_rank', 'position')


class StaffProfileSerializer(serializers.ModelSerializer):
    staff = StaffSerializer(read_only=True)

    class Meta:
        model = StaffProfile
        fields = ('id', 'staff', 'avatar')