from django.db import models
from django.contrib import admin
from phonenumbers import parse, is_valid_number
from django.core.exceptions import ValidationError

class Contact(models.Model):
    idContact = models.BigAutoField(primary_key=True
                                   )
    date = models.DateField(auto_now=True,
                            )
    
    name = models.CharField(max_length=100
                            )

    phone = models.CharField(max_length=20
                             )
    
    email = models.EmailField()

    company = models.CharField(max_length=255,
                               blank=True,
                               null=True
                               )

    message = models.TextField()

    reviewed = models.BooleanField(default=False)  

    def clean(self):
        super().clean()
        parsed_phone = parse(self.phone, None)
        
        if not is_valid_number(parsed_phone):
            raise ValidationError("Phone number not valid")

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Contact, self).save(*args, **kwargs)
    
    class Meta:
       db_table = 'Contact'
       verbose_name_plural = '01 Contact'
       ordering = ['-date', '-idContact']

class ContactAdmin(admin.ModelAdmin):
        list_display = ('name', 'phone', 'email', 'reviewed')