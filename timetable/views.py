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
def get_timetable(request):
    user = request.user
    list = []
    student = Students.objects.get(user=user)
    group_enrollment = Group_Enrollment.objects.get(student_id=student)
    group = group_enrollment.group_id
    for t in Timetable.objects.filter(group=group):
        data = {"day_of_week": t.day_of_week, "lesson_type": t.lesson_type, "subject": t.enrollment.subject.title, "teacher name": t.enrollment.lecturer.user.first_name, "teacher surname": t.enrollment.lecturer.user.last_name, "start_time": t.start_time, "finish_time": t.finish_time, "room_number": t.room_number}
        list.append(data)
    return Response(list)



@api_view(('GET',))
def get_timetable_by_staff(request):
    user = request.user
    list = []
    staff = request.data.get('staff_id')
    enrollment = Enrollment.objects.filter(lecturer=staff).first()
    for t in Timetable.objects.filter(enrollment=enrollment):
        data = {"day_of_week": t.day_of_week, "lesson_type": t.lesson_type, "subject": t.enrollment.subject.title, "teacher name": t.enrollment.lecturer.user.first_name, "teacher surname": t.enrollment.lecturer.user.last_name, "start_time": t.start_time, "finish_time": t.finish_time, "room_number": t.room_number}
        list.append(data)
    return Response(list)

   

@api_view(('GET',))
def get_timetable_by_room(request):
    serializer_class = TimetableSerialaizer
    list = []
    room_number = request.data.get('room_number')
    for t in Timetable.objects.filter(room_number=room_number):
        data = {"day_of_week": t.day_of_week, "lesson_type": t.lesson_type, "subject": t.enrollment.subject.title, "teacher name": t.enrollment.lecturer.user.first_name, "teacher surname": t.enrollment.lecturer.user.last_name, "start_time": t.start_time, "finish_time": t.finish_time, "room_number": t.room_number}
        list.append(data)
    return Response(list)


@api_view(('GET',))
def get_timetable_by_group(request):
    serializer_class = TimetableSerialaizer
    list = []
    group = request.data.get('group_id')
    for t in Timetable.objects.filter(group=group):
        data = {"day_of_week": t.day_of_week, "lesson_type": t.lesson_type, "subject": t.enrollment.subject.title, "teacher name": t.enrollment.lecturer.user.first_name, "teacher surname": t.enrollment.lecturer.user.last_name, "start_time": t.start_time, "finish_time": t.finish_time, "room_number": t.room_number}
        list.append(data)
    return Response(list)
