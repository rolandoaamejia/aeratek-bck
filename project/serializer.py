from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Projects, ImageProjects

# SERIALIZER FOR TABLES
class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'

    @action(detail=True, methods=['POST'])
    def add_image(self, request, pk=None):
        service = self.get_object()
        image_data = request.data
        image_serializer = ImageProjectsSerializer(data=image_data)

        if image_serializer.is_valid():
            image_serializer.save()
            service.Images.add(image_serializer.instance)
            return Response(image_serializer.data, status=201)
        else:
            return Response(image_serializer.errors, status=400)

class ImageProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageProjects
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['idtitle'] = ProjectsSerializer(instance.idtitle).data

        return response