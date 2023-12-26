from django.db import models
from django.http import JsonResponse
from django.shortcuts import render

# Create your models here.
# Create the images that will appear on 
class ImageNews(models.Model):
    idImageNews = models.BigAutoField(primary_key=True)

    date = models.DateField(auto_now=True,
                            )
    
    image = models.ImageField(upload_to='imageNews/')

    description = models.CharField(max_length=255)

    def __str__(self):
        return "Description " + self.description
    class Meta:
        db_table = 'ImageNews'
        verbose_name_plural = '02 Images News'
        ordering = ['-date']
    
class News(models.Model):
    idNews = models.BigAutoField(primary_key=True)
    date = models.DateField(auto_now=True,
                            )
    
    title = models.CharField(db_column='title',
                            max_length=255,
                            null=True, 
                            blank=True,
                            verbose_name='New Title'
                            )
    
    titulo = models.CharField(db_column='titulo',
                            max_length=255,
                            null=True, 
                            blank=True,
                            verbose_name='Titulo noticia en Español'
                            )
    
    body = models.TextField(db_column='body',
                            verbose_name='New Body'
                            )
    
    cuerpo = models.TextField(db_column='cuerpo',
                            verbose_name='Cuerpo de la noticia en Español'
                            )

    coverImage =  models.ImageField(upload_to='coverNewsImage/')

    Images = models.ManyToManyField(ImageNews, blank=True)
    
    def __str__(self):
        file = "New Title: " + self.title
        return file 
    
    class Meta:
        db_table = 'News'
        verbose_name_plural = '01 News'
        ordering = ['-date']

def service_detail_json(request, service_id):
    news = News.objects.get(pk=service_id)
    images = ImageNews.objects.filter(pk__in=news.Images.all())
    image_urls = [image.image.url for image in images]

    # Crear un diccionario JSON con las URLs de las imágenes
    response_data = {
        'news_title': news.title,
        'news_body': news.body,
        'news_image_urls': image_urls
    }

    return JsonResponse(response_data)