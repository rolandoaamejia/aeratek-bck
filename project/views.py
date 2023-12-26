import datetime as dt
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone

from rest_framework.decorators import api_view
from rest_framework.response import Response 

from rest_framework import viewsets
from .serializer import ProjectsSerializer, ImageProjectsSerializer

from datetime import datetime, timedelta, date, time


from rest_framework.generics import ListAPIView

from .models import Projects, ImageProjects

# Create your views here.
class ProjectsView(viewsets.ModelViewSet):
    serializer_class = ProjectsSerializer
    #permission_classes = [IsAuthenticated]
    queryset = Projects.objects.all()

class ImageProjectsView(viewsets.ModelViewSet):
    serializer_class = ImageProjectsSerializer
    #permission_classes = [IsAuthenticated]
    queryset = ImageProjects.objects.all()

@api_view(['GET'])
def ProjectsDetailView(request, service_id):
    try:
        service = Projects.objects.get(pk=service_id)
        
        # Filters the images by the specific Project
        images = ImageProjects.objects.filter(pk__in=service.Images.all())
        image_urls = [image.image.url for image in images]
        
        response_data = {
            'project_title': service.title,
            'project_titulo': service.titulo,
            'project_body': service.body,
            'project_cuerpo': service.cuerpo,
            'image_urls': image_urls
        }

        return JsonResponse(response_data)
    except Projects.DoesNotExist:
        return JsonResponse({'error': 'The service does not exists'}, status=404)