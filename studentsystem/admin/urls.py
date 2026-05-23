from django.urls import path

from . import views

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('home/', views.home_redirect, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_redirect, name='dashboard'),
    path('admin-dashboard/', views.dashboard, name='admin_dashboard'),
]
