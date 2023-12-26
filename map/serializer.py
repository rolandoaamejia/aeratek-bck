from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Maps

# SERIALIZER PARA TABLAS 
class MapsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maps
        fields = '__all__'