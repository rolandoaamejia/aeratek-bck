from django.db import models

# Create your models here.
class Footer(models.Model):
    idFooter = models.BigAutoField(db_column='idAboutUs',
                                    primary_key=True,
                                    )
    
    date = models.DateField(auto_now=True,
                            )
    
    title = models.CharField(db_column='title',
                            max_length=255,
                            null=True, 
                            blank=True,
                            verbose_name='Title Footer'
                            )
    
    titulo = models.CharField(db_column='titulo',
                            max_length=255,
                            null=True, 
                            blank=True,
                            verbose_name='Titulo footer Español'
                            )
    
    date = models.DateField(auto_now=True,
                            )
    
    body = models.TextField(db_column='body',
                            verbose_name='Body Footer',
                            ) 
    
    cuerpo = models.TextField(db_column='cuerpo',
                            verbose_name='cuerpo Footer',
                            ) 
    
    def __str__(self):
      file = "title" + self.title
      return file

    class Meta:
        db_table = 'Footer'
        verbose_name_plural = '01 Footer'
        ordering = ['-date']