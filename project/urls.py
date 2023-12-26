from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from project import views

# api versioning
router = routers.DefaultRouter()
router.register(r'projects', views.ProjectsView, 'projects')
router.register(r'imagesprojects', views.ImageProjectsView, 'imagesprojects')


urlpatterns = [
    path("", include(router.urls)),
    path("projects/", views.ProjectsView.as_view({'get': 'list'}), name="projects"),
    path('ProjectsDetailView/<int:service_id>/', views.ProjectsDetailView, name='projects_detail_json'),
    path('docs/', include_docs_urls(title="aeratekCMS API"))
]