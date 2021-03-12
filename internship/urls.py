from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('internships', views.internships, name='internships'),
    path('internships/detail', views.detail, name='detail'),
]