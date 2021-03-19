from django.urls import path
from . import views

urlpatterns = [
    path('auth-company', views.auth_company, name='auth_company'),
]
