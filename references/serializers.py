from rest_framework import serializers

from students.serializers import StudentsSerializer
from .models import Reference_Type, Reference, Student_Reference


class ReferenceTypeSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = Reference_Type
        fields = ('id', 'name', 'template')


class ReferenceSerializer(serializers.ModelSerializer):
    reference_type = ReferenceTypeSerialaizer(read_only=True)
    class Meta:
        model = Reference
        fields = ('id', 'reference_type', 'description')


class StudentReferenceSerializer(serializers.ModelSerializer):
    student = StudentsSerializer(read_only=True)
    reference = ReferenceSerializer(read_only=True)
    class Meta:
        model = Student_Reference
        fields = ('id', 'student', 'reference')
