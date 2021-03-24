from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='std_home'),
    path('internships', views.internships, name='internships'),
    path('internships/detail/<int:post_id>/', views.detail, name='detail'),
    path('auth-student', views.auth_student, name='auth_student'),
    path('profile', views.profile, name='profile'),
    path('profileEdit', views.profileEdit, name='profileEdit'),
    path('dashboard', views.dashboard, name='dashboard'),
]