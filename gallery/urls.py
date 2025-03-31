from django.urls import path
from . import views

urlpatterns = [
    path('', views.image_list, name='image_list'),
    path('upload/', views.upload_image, name='upload_image'),
    path('edit/<int:image_id>/', views.edit_image, name='edit_image'),
    path('delete/<int:image_id>/', views.delete_image, name='delete_image'),
    path('download/<int:image_id>/', views.download_image, name='download_image'),
    # Fix the URL pattern to match the view function parameter names
    path('apply_filter/<str:filter_type>/<int:image_id>/', views.apply_filter, name='apply_filter'),
]