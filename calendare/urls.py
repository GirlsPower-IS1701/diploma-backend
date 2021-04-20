from django.urls import path, re_path
from . import views


urlpatterns = [
    path('api/academ_calendar', views.AcademicCalendarApi.as_view(), name='academ_calendar'),
    path('api/calendar_events', views.EventsApi.as_view(), name='calendar_events'),
    path('api/get_calendar_events', views.get_calendar_events)
]