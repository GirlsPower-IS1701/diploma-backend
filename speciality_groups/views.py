from django.shortcuts import render
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from students.models import Students
from .models import Grades
from .serializers import GradesSerializer

@api_view(('GET',))
@permission_classes([IsAuthenticated, ])
def get_study_plan(request):
    grades = []
    user = request.user
    student = Students.objects.get(user=user)
    for g in Grades.objects.filter(student=student):
        enrollment = g.enrollment
        subject = enrollment.subject.title
        study_plan = {'subject': subject, 'pk1': g.pk1, 'pk2': g.pk2, 'final': g.final_grade, 'grade_letter': g.grade_letter, 'gpa': g.gpa}
        grades.append(study_plan)

    return Response(grades)

@api_view(('GET',))
@permission_classes([IsAuthenticated, ])
def calculate_gpa(request):
    credits_count = 0
    total = 0
    user = request.user
    student = Students.objects.get(user=user)
    list = []
    data = []
    for g in Grades.objects.filter(student=student):
        data.append(GradesSerializer(g).data)
        enrollment = g.enrollment
        subject = enrollment.subject
        credits_count += int(subject.credits_count)
        total = subject.credits_count * int(g.gpa)
        list.append(total)
    total_sum = 0
    for i in list:
        total_sum+=i

    res = int(total_sum/credits_count)
    return Response({"grades": data, "gpa": res})



# @api_view(('GET',))
# @permission_classes([IsAuthenticated, ])
# def calculate_gpa_example(request):
#     credits_count = 0
#     total = 0
#     user = request.user
#     student = Students.objects.get(user=user)
#     list = []
#     data = []
#     for g in Grades.objects.filter(student=student):
        
#         enrollment = g.enrollment
#         subject = enrollment.subject
#         data.append({"subject": subject.title, "pk1": g.pk1, "pk2": g.pk2, "exam": g.exam_grade, "final": g.final_grade, "gpa": g.gpa})
#         credits_count += int(subject.credits_count)
#         total = subject.credits_count * int(g.gpa)
#         list.append(total)
#     total_sum = 0
#     for i in list:
#         total_sum+=i

#     res = int(total_sum/credits_count)
#     return Response({"grades": data, "gpa": res})

@api_view(('GET',))
@permission_classes([IsAuthenticated, ])
def calculate_gpa_example(request):
    credits_count = 0
    total = 0
    user = request.user
    student = Students.objects.get(user=user)
    list = []
    data = []
    for g in Grades.objects.filter(student=student):
        
        enrollment = g.enrollment
        subject = enrollment.subject
        data.append({"subject": subject.title, "pk1": g.pk1, "pk2": g.pk2, "exam": g.exam_grade, "final": g.final_grade, "gpa": g.gpa})
        credits_count += int(subject.credits_count)
        total = subject.credits_count * int(g.gpa)
        list.append(total)
    total_sum = 0
    for i in list:
        total_sum+=i

    res = int(total_sum/credits_count)
    return Response({"grades": data, "gpa": res})






