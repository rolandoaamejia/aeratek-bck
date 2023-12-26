from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Footer

# SERIALIZER PARA TABLAS 
class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = '__all__'