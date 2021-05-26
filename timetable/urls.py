from django.urls import path, re_path
from . import views

from .views import get_timetable_by_group, get_timetable_by_staff

urlpatterns = [
    path('api/timetable/', views.get_timetable),
    path('api/timetable/filter_by_staff/', views.get_timetable_by_staff),
    path('api/timetable/filter_by_room/', views.get_timetable_by_room),
    path('api/timetable/filter_by_group/', views.get_timetable_by_group),
]