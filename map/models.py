from django.db import models

# Create your models here.
class Maps(models.Model):
    idMap = models.BigAutoField(primary_key=True
                                   )
    
    date = models.DateField(auto_now=True,
                            )
    
    title = models.CharField(db_column='title',
                            max_length=255,
                            null=True, 
                            blank=True,
                            verbose_name='Map Title'
                            )
    
    image = models.ImageField(upload_to='map/',blank=True,null=True)

    def __str__(self):
        file = self.title
        return file
    
    class Meta:
       db_table = 'Maps'
       verbose_name_plural = '01 Map'
       ordering = ['-date']