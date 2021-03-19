from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('auth-student', views.auth_student, name='auth_student'),   
    path('profile', views.profile, name='profile'),   
    path('profileedit', views.profileEdit, name='profileedit'),   
]