from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from service import views

# api versioning
router = routers.DefaultRouter()
router.register(r'services', views.ServicesView, 'services')
router.register(r'imageservice', views.ImageServiceView, 'imageservices')


urlpatterns = [
    path("", include(router.urls)),
    path('ServiceDetailView/<int:service_id>/', views.ServiceDetailView, name='service_detail_json'),
    path('docs/', include_docs_urls(title="aeratekCMS API"))
]

