from django.db import models
from django.http import JsonResponse
from django.shortcuts import render

# Create your models here.
# Create the images that will appear on 
class ImageService(models.Model):
    idImageServices = models.BigAutoField(primary_key=True)

    date = models.DateField(auto_now=True,
                            )
    
    image = models.ImageField(upload_to='imageServices/')

    description = models.CharField(max_length=255)

    def __str__(self):
        return "Descripcion " + self.description
    class Meta:
        db_table = 'ImageService'
        verbose_name_plural = '02 Images Services'
        ordering = ['-date']
    
class Services(models.Model):
    idServices = models.BigAutoField(primary_key=True)
    date = models.DateField(auto_now=True,
                            )
    
    title = models.CharField(db_column='title',
                            max_length=255,
                            null=True, 
                            blank=True,
                            verbose_name='Service Title'
                            )
    
    titulo = models.CharField(db_column='titulo',
                            max_length=255,
                            null=True, 
                            blank=True,
                            verbose_name='Titulo del Servicio'
                            )
    
    body = models.TextField(db_column='body',
                            verbose_name='Service Body'
                            )
    
    cuerpo = models.TextField(db_column='cuerpo',
                            verbose_name='Cuerpo del Servicio en Español'
                            )

    coverImage =  models.ImageField(upload_to='coverServicesImage/')

    Images = models.ManyToManyField(ImageService, blank=True)
    
    def __str__(self):
        file = "Service Title: " + self.title
        return file 
    
    class Meta:
        db_table = 'Services'
        verbose_name_plural = '01 Services'
        ordering = ['-date']

def service_detail_json(request, service_id):
    service = Services.objects.get(pk=service_id)
    images = ImageService.objects.filter(pk__in=service.Images.all())
    image_urls = [image.image.url for image in images]

    # Crear un diccionario JSON con las URLs de las imágenes
    response_data = {
        'service_title': service.title,
        'service_body': service.body,
        'image_urls': image_urls
    }

    return JsonResponse(response_data)