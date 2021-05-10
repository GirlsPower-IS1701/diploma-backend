from django.shortcuts import render
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.utils import is_student
from accounts.models import User
from students.models import Students
from .models import Grades
from .serializers import GradesSerializer

# Create your views here.
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
