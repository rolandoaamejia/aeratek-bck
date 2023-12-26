from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from banners import views

# api versioning
router = routers.DefaultRouter()
router.register(r'banners', views.BannersView, 'banners')

urlpatterns = [
    path("", include(router.urls)),
    path('docs/', include_docs_urls(title="aeratekCMS API"))
]

