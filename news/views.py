import datetime as dt
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone

from rest_framework.decorators import api_view
from rest_framework.response import Response 

from rest_framework import viewsets
from .serializer import NewsSerializer, ImagesNewSerializer

from datetime import datetime, timedelta, date, time


from rest_framework.generics import ListAPIView

from .models import News, ImageNews

# Create your views here.
class NewsView(viewsets.ModelViewSet):
    serializer_class = NewsSerializer
    #permission_classes = [IsAuthenticated]
    queryset = News.objects.all()

class ImagesNewView(viewsets.ModelViewSet):
    serializer_class = ImagesNewSerializer
    #permission_classes = [IsAuthenticated]
    queryset = ImageNews.objects.all()


def NewsDetailView(request, service_id):
    try:
        news = News.objects.get(pk=service_id)
        
        # Filters the images by the specific Project
        images = ImageNews.objects.filter(pk__in=news.Images.all())
        image_urls = [image.image.url for image in images]
        
        response_data = {
            'news_title': news.title,
            'titulo': news.titulo,
            'news_body': news.body,
            'cuerpo': news.cuerpo,
            'image_urls': image_urls
        }

        return JsonResponse(response_data)
    except News.DoesNotExist:
        return JsonResponse({'error': 'The new does not exists'}, status=404)
