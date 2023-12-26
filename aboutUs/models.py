from django.db import models

# Create your models here.
class AboutUs(models.Model):
    idAboutUs = models.BigAutoField(db_column='idAboutUs',
                                    primary_key=True,
                                    )
    
    date = models.DateField(auto_now=True,
                            )
    
    title = models.CharField(db_column='title',
                            max_length=255,
                            null=True, 
                            blank=True,
                            verbose_name='Title About Us'
                            ) 
    
    titulo = models.CharField(db_column='titulo',
                              max_length=255,
                              null=True,
                              blank=True,
                              verbose_name="Titulo en Español"
                              )
    
    body = models.TextField(db_column='body',
                            verbose_name='Body About Us',
                            ) 
    
    cuerpo = models.TextField(db_column='cuerpo',
                              verbose_name='Cuerpo en Español Acerca de Nosotros',
                              )
    def __str__(self):
      file = "title" + self.title
      return file

    class Meta:
        db_table = 'AboutUs'
        verbose_name_plural = '01 About Us'
        ordering = ['-date']