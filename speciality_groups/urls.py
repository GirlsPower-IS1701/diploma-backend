from django.urls import path, re_path
from . import views
from rest_framework_simplejwt import views as jwt_views
from knox import views as knox_views
from .views import get_study_plan

urlpatterns = [
    path('api/study_plan/', views.get_study_plan),
    path('api/get_gpa/', views.calculate_gpa),
]