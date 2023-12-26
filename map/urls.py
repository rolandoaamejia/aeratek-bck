from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from map import views

# api versioning
router = routers.DefaultRouter()
router.register(r'maps', views.MapsView, 'maps')

urlpatterns = [
    path("", include(router.urls)),
    path('docs/', include_docs_urls(title="aeratekCMS API"))
]