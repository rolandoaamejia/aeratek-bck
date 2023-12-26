from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import News, ImageNews

# SERIALIZER PARA TABLAS 
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

    @action(detail=True, methods=['POST'])
    def add_image(self, request, pk=None):
        news = self.get_object()
        image_data = request.data
        image_serializer = ImagesNewSerializer(data=image_data)

        if image_serializer.is_valid():
            image_serializer.save()
            news.Images.add(image_serializer.instance)
            return Response(image_serializer.data, status=201)
        else:
            return Response(image_serializer.errors, status=400)

class ImagesNewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageNews
        fields = '__all__'

        # FUNCTION TO SEND FOREIGN KEYS TO JSON 
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['idtitle'] = NewsSerializer(instance.idtitle).data

        return response