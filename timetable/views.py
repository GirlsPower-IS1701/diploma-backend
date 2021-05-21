from django.shortcuts import render
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from students.models import Students
from .models import Timetable
from speciality_groups.models import Group_Enrollment, Enrollment
from .serializers import TimetableSerialaizer

@api_view(('GET',))
def get_timetable_by_group(request):
    user = request.user
    student = Students.objects.get(user=user)
    group_enrollment = Group_Enrollment.objects.get(student_id=student)
    group = group_enrollment.group_id
    timetable = Timetable.objects.filter(group=group)
    serializer = TimetableSerialaizer(timetable, many=True)
    return Response(serializer.data)



@api_view(('POST',))
def get_timetable_by_staff(request):
    user = request.user
    staff = request.data.get('staff_id')
    enrollment = Enrollment.objects.filter(lecturer=staff).first()
    timetable = Timetable.objects.filter(enrollment=enrollment)
    serializer = TimetableSerialaizer(timetable, many=True)
    return Response(serializer.data)