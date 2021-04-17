from rest_framework import serializers

from accounts.serializers import UserSerializer
from .models import Payment_Form, Degree_Types, Study_Form, Study_Statuses, Students


class PaymentFormSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = Payment_Form
        fields = ('id', 'description')


class DegreeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Degree_Types
        fields = ('id', 'title')


class StudyFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Study_Form
        fields = ('id', 'description', 'course_count')

class StudyStatusesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Study_Statuses
        fields = ('id', 'title')

class StudentsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    study_status = StudyStatusesSerializer(read_only=True)
    study_form = StudyFormSerializer(read_only=True)
    payment_form = PaymentFormSerialaizer(read_only=True)

    class Meta:
        model = Students
        fields = ('id', 'user', 'study_status', 'study_form', 'payment_form', 'course')
