from django.contrib import admin
from .models import Projects, ImageProjects

# Register your models here.
admin.site.register(Projects)
admin.site.register(ImageProjects)

## Template Info
admin.site.site_header = "AeraTek Administration"
admin.site.site_title = "Admin AeraTeK"
admin.site.index_title = "Admin AeraTek"