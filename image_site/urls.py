"""
URL configuration for image_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gallery import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.image_list, name='image_list'),
    path('upload/', views.upload_image, name='upload_image'),
    path('download/<int:image_id>/', views.download_image, name='download_image'),
    path('edit/<int:image_id>/', views.edit_image, name='edit_image'),
    path('apply_filter/<str:filter_type>/<int:image_id>/', views.apply_filter, name='apply_filter'),
    path('delete/<int:image_id>/', views.delete_image, name='delete_image'),
]
