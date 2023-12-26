from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from news import views

# api versioning
router = routers.DefaultRouter()
router.register(r'news', views.NewsView, 'news')
router.register(r'imagesnew', views.ImagesNewView, 'imagesnew')


urlpatterns = [
    path("", include(router.urls)),
    path('NewsDetailView/<int:service_id>/', views.NewsDetailView, name='news_detail_json'),
    path('docs/', include_docs_urls(title="aeratekCMS API"))
]