from django.db import models

# Create your models here.
class Banners(models.Model):
    idBanner = models.BigAutoField(primary_key=True
                                   )
    
    date = models.DateField(auto_now=True,
                            )
    
    title = models.CharField(db_column='title',
                            max_length=255,
                            null=True, 
                            blank=True,
                            verbose_name='Banner Title'
                            )
    
    titulo =  models.CharField(db_column='titulo',
                            max_length=255,
                            null=True, 
                            blank=True,
                            verbose_name='Titulo en Español'
                            )
    
    image = models.ImageField(upload_to='banners/',blank=True,null=True)

    def __str__(self):
        file = self.title
        return file
    
    class Meta:
       db_table = 'Banners'
       verbose_name_plural = '01 Banners'
       ordering = ['-date']
