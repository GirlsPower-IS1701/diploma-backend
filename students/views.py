from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import User
from accounts.utils import is_student
from students.models import Students, Study_Statuses, Study_Form, Payment_Form, Degree_Types, StudentProfile
from students.serializers import StudentsSerializer, StudentProfileSerializer
from django.contrib.auth.models import Group


class StudentApi(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = StudentsSerializer

    def get(self, request, *args, **kwargs):
        students = Students.objects.all()
        serializer = self.serializer_class(students, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            student = Students(
                user = User.objects.get(pk=request.POST["user_id"]),
                study_status=Study_Statuses.objects.get(pk=request.POST["study_status_id"]),
                study_form=Study_Form.objects.get(pk=request.POST["study_form_id"]),
                payment_form = Payment_Form.objects.get(pk=request.POST["payment_form_id"]),
                degree_type = Degree_Types.objects.get(pk=request.POST["degree_type_id"]),
                course=serializer.validated_data.get("course")
            )
            student.save()

            user = User.objects.get(pk=request.POST["user_id"])
            group = Group.objects.get(name='Student')
            group.user_set.add(user)

            response_serializer = self.serializer_class(student)
            return Response(response_serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



class StudentProfileApi(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = StudentProfileSerializer

    def get(self, request, *args, **kwargs):
        student = Students.objects.get(user=request.user)
        student_profile = StudentProfile.objects.get(student=student)
        serializer = self.serializer_class(student_profile)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            student_profile = StudentProfile(
                student = Students.objects.get(user=request.user),
                avatar=serializer.validated_data.get("avatar")
            )
            student_profile.save()
            response_serializer = self.serializer_class(student_profile)
            return Response(response_serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(('GET',))
@permission_classes([IsAuthenticated, ])
def get_student_profile(request):
    user = request.user
    if is_student(user):
        student = Students.objects.get(user=user)
        student_profile = StudentProfile.objects.get(student=student)
        student_serializer = StudentsSerializer(student)
        profile_serializer = StudentProfileSerializer(student_profile)
        if profile_serializer.data['avatar']:
            return Response({"student": student_serializer.data, "avatar": profile_serializer.data['avatar']})
        else:
            return Response({"student": student_serializer.data, "avatar": None})
    else:
        return Response({"You don't have permissions for this action"})