from django.urls import path
from django.contrib.auth import views as auth_views
from mainapp import views

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='mainapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='mainapp/logout.html'), name='logout'),
    path('choose/', views.choose, name='choose'),
    path('session/', views.session, name='session'),
    path('analysis/', views.analysis, name='analysis'),
]
