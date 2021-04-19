from django.urls import path, re_path
from . import views
from rest_framework_simplejwt import views as jwt_views
from knox import views as knox_views
from .views import StaffApi

urlpatterns = [
    path('api/staff/', views.StaffApi.as_view(), name='staff_api'),
    path('api/staff_profile', views.StaffProfileApi.as_view(), name='staff_profile')
]