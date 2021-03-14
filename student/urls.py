from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('auth-student', views.auth_student, name='auth_student'),   
    path('logout', LogoutView.as_view(), {'next_page': '/'}, name='logout'), 
]