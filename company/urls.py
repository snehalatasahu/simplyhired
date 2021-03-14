from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('auth-company', views.auth_company, name='auth_company'),
    path('logout', LogoutView.as_view(), {'next_page': '/'}, name='logout'), 
]
