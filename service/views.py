import datetime as dt
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone

from rest_framework.decorators import api_view
from rest_framework.response import Response 

from rest_framework import viewsets
from .serializer import ServicesSerializer, ImageServiceSerializer

from datetime import datetime, timedelta, date, time


from rest_framework.generics import ListAPIView

from .models import Services, ImageService

# Create your views here.
class ServicesView(viewsets.ModelViewSet):
    serializer_class = ServicesSerializer
    #permission_classes = [IsAuthenticated]
    queryset = Services.objects.all()

class ImageServiceView(viewsets.ModelViewSet):
    serializer_class = ImageServiceSerializer
    #permission_classes = [IsAuthenticated]
    queryset = ImageService.objects.all()

@api_view(['GET'])
def ServiceDetailView(request, service_id):
    try:
        service = Services.objects.get(pk=service_id)
        
        # Filters the images by the specific Service
        images = ImageService.objects.filter(pk__in=service.Images.all())
        image_urls = [image.image.url for image in images]
        
        response_data = {
            'service_title': service.title,
            'service_titulo': service.titulo,
            'service_body': service.body,
            'service_cuerpo': service.cuerpo,
            'image_urls': image_urls
        }

        return JsonResponse(response_data)
    except Services.DoesNotExist:
        return JsonResponse({'error': 'The service does not exists'}, status=404)