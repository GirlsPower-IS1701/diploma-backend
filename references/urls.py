from django.urls import path, re_path
from . import views


urlpatterns = [
    path('api/references/', views.ReferenceApiView.as_view()),
    re_path('api/gethistory/', views.get_reference_history),
]