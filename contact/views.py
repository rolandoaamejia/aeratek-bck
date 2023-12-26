import datetime as dt
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone

from rest_framework.decorators import api_view
from rest_framework.response import Response 

from rest_framework import viewsets
from .serializer import ContactSerializer

from datetime import datetime, timedelta, date, time


from rest_framework.generics import ListAPIView

from .models import Contact

# Create your views here.
class ContactView(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    #permission_classes = [IsAuthenticated]
    queryset = Contact.objects.all()