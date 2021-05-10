from rest_framework import serializers
from departments.serializers import DepartmentSerialaizer, SubjectsSerializer
from staff.serializers import StaffSerializer
from students.serializers import StudentsSerializer
from .models import Adviser, Group, Enrollment, Grades

class AdviserSerialaizer(serializers.ModelSerializer):
    staff = StaffSerializer(read_only=True)
    class Meta:
        model = Adviser
        fields = ('id', 'staff')


class GroupSerailizer(serializers.ModelSerializer):
    department = DepartmentSerialaizer(read_only=True)
    adviser = AdviserSerialaizer(read_only=True)
    class Meta:
        model = Group
        fields = ('id', 'department', 'adviser', 'start_year', 'finish_year')


class EnrollmentSerializer(serializers.ModelSerializer):
    subject = SubjectsSerializer(read_only=True)
    group = GroupSerailizer(read_only=True)
    lecturer = StaffSerializer(read_only=True)
    tutor = StaffSerializer(read_only=True)
    class Meta:
        model = Enrollment
        fields = ('id', 'subject', 'group', 'lecturer', 'tutor', 'semester')


class GradesSerializer(serializers.ModelSerializer):
    enrollment = EnrollmentSerializer(read_only=True)
    student = StudentsSerializer(read_only=True)
    class Meta:
        model = Grades
        fields = ('id', 'enrollment', 'student', 'pk1', 'pk2', 'exam_grade', 'final_grade', 'grade_letter', 'gpa')