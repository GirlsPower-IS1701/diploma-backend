from django.shortcuts import render
from .models import News
from .serializers import NewsSerializer
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated



@api_view(('GET',))
@permission_classes([IsAuthenticated, ])
def get_news(request):
    news = News.objects.filter().order_by('-created_at')
    serializer = NewsSerializer(news, many=True)
    return Response(serializer.data)