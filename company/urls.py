from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('auth-company', views.auth_company, name='auth_company'),
    path('post-detail/<int:post_id>/', views.post_detail, name='post-detail'),
    path('new-post', views.new_post, name='new-post'),
    path('profile', views.company_profile, name='company-profile'),
    path('profile-edit', views.company_profile_edit, name='company-profile-edit'),
]

