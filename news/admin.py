from django.contrib import admin
from .models import News, ImageNews

# Register your models here.
admin.site.register(News)
admin.site.register(ImageNews)

## Template Info
admin.site.site_header = "AeraTek Administration"
admin.site.site_title = "Admin AeraTeK"
admin.site.index_title = "Admin AeraTek"