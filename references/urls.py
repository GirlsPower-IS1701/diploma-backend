from django.urls import path, re_path
from . import views


urlpatterns = [
    path('api/references/', views.ReferenceApiView.as_view()),
    path('api/references/history', views.get_student_reference_history),
]