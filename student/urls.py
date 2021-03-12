from django.urls import path
from . import views

urlpatterns = [
    path('auth-student', views.auth_student, name='auth_student'),    
]