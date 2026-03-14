from django.urls import path
from . import views

urlpatterns = [
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('upload-movie/', views.upload_movie, name='upload_movie'),
    path('edit-movie/<int:movie_id>/', views.edit_movie, name='edit_movie'),
    path('delete-movie/<int:movie_id>/', views.delete_movie, name='delete_movie'),
]
