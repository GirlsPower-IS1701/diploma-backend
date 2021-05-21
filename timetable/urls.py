from django.urls import path, re_path
from . import views

from .views import get_timetable_by_group, get_timetable_by_staff

urlpatterns = [
    path('api/timetable/', views.get_timetable_by_group),
    path('api/timetable/staff/', views.get_timetable_by_staff),
]