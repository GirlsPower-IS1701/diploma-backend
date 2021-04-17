from rest_framework import serializers
from .models import Department, Subject_Cycles, Subjects, Cafedra_Subjects


class DepartmentSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name')


class SubjectCycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject_Cycles
        fields = ('id', 'title', 'short_title')


class SubjectsSerializer(serializers.ModelSerializer):
    subject_cycle = SubjectCycleSerializer(read_only=True)
    class Meta:
        model = Subjects
        fields = ('id', 'code', 'description', 'subject_cycle', 'lection_count', 'lab_count', 'practice_count', 'is_additional', 'is_language', 'is_research', 'is_practice', 'credits_count')


class CafedraSubjectsSerializer(serializers.ModelSerializer):
    subject_id = SubjectsSerializer(read_only=True)
    department_id = DepartmentSerialaizer(read_only=True)
    class Meta:
        model = Cafedra_Subjects
        fields = ('id', 'subject_id', 'department_id')