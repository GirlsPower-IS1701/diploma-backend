from rest_framework import serializers

from .models import Academic_Calendar, Events

class AcademicCalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Academic_Calendar
        fields = ('id', 'name', 'from_year', 'to_year')


class EventsSerializer(serializers.ModelSerializer):
    academic_calendar = AcademicCalendarSerializer(read_only=True)

    class Meta:
        model = Events
        fields = ('id', 'name', 'academic_calendar', 'semester', 'from_date', 'to_date')
