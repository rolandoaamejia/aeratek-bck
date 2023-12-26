from django.db import models
from django.http import JsonResponse
from django.shortcuts import render

# Create your models here.
# Create the images that will appear on 
class ImageProjects(models.Model):
    idImageProjects = models.BigAutoField(primary_key=True)

    date = models.DateField(auto_now=True,
                            )
    
    image = models.ImageField(upload_to='imageProjects/')

    description = models.CharField(max_length=255)

    def __str__(self):
        file = "Description: " + self.description
        return file
    
    class Meta:
        db_table = 'ImageProjects'
        verbose_name_plural = '02 Images Projects'
        ordering = ['-date']
    
class Projects(models.Model):
    idProjects = models.BigAutoField(primary_key=True)
    date = models.DateField(auto_now=True,
                            )
    
    date_project = models.DateField(blank=False, null=False)
    
    title = models.CharField(db_column='title',
                            max_length=255,
                            null=True, 
                            blank=True,
                            verbose_name='Project Title'
                            )
    
    titulo = models.CharField(db_column='titulo',
                            max_length=255,
                            null=True, 
                            blank=True,
                            verbose_name='Titulo del Proyecto en Español'
                            )
    
    body = models.TextField(db_column='body',
                            verbose_name='Project Body'
                            )
    
    cuerpo = models.TextField(db_column='cuerpo',
                            verbose_name='Descripcion del Proyecto en Español'
                            )

    coverImage =  models.ImageField(upload_to='coverProjectsImage/')

    Images = models.ManyToManyField(ImageProjects, blank=True)
    
    def __str__(self):
        file = "Project Title: " + self.title
        return file 
    
    class Meta:
        db_table = 'Projects'
        verbose_name_plural = '01 Projects'
        ordering = ['-date']

def service_detail_json(request, service_id):
    service = Projects.objects.get(pk=service_id)
    images = ImageProjects.objects.filter(pk__in=service.Images.all())
    image_urls = [image.image.url for image in images]

    # Json Directory for Images Urls
    response_data = {
        'service_title': service.title,
        'service_body': service.body,
        'image_urls': image_urls
    }

    return JsonResponse(response_data)