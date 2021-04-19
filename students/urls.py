from django.urls import path, re_path
from . import views
from rest_framework_simplejwt import views as jwt_views
from knox import views as knox_views
from .views import StudentApi

urlpatterns = [
    path('api/students/', views.StudentApi.as_view(), name='students_api'),
    path('api/student_profile', views.StudentProfileApi.as_view(), name='student_profile')
]