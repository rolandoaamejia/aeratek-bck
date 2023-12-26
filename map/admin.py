from django.contrib import admin
from .models import Maps

# Register your models here.
admin.site.register(Maps)

## Template Info
admin.site.site_header = "AeraTek Administration"
admin.site.site_title = "Admin AeraTeK"
admin.site.index_title = "Admin AeraTek"