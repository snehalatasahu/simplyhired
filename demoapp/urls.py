from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('auth-student', views.auth_student, name='auth_student'),
    path('auth-company', views.auth_company, name='auth_company'),
    path('internships', views.internships, name='internships'),
    path('internships/detail', views.detail, name='detail'),

    
]