from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('internships', views.internships, name='internships'),
    path('internships/detail', views.detail, name='detail'),
    path('auth-student', views.auth_student, name='auth_student'),   
    path('profile', views.profile, name='profile'),   
    path('profileedit', views.profileEdit, name='profileedit'),   
]