from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Contact

# SERIALIZER FOR TABLES 
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'