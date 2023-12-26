from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Banners

# SERIALIZER PARA TABLAS 
class BannersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banners
        fields = '__all__'