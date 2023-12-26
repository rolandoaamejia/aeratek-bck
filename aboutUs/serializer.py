from rest_framework import serializers
from django.contrib.auth.models import User
from .models import AboutUs

# SERIALIZER PARA TABLAS 
class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'