from django.conf.urls import url
from django.urls import path, re_path, include
from . import views
from rest_framework_simplejwt import views as jwt_views
from .views import RegisterAPI, LoginAPI, ChangePasswordView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('api/privacy', views.index, name='index'),

    # path('api/logout/', views.LogoutView.as_view()),
    # path('api/login/', LoginAPI.as_view(), name='login'),
    # path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]