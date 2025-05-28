from django.urls import path
from  . import views
from django.contrib.auth import views as auth_views
from .views import CustomLoginView

urlpatterns = [
   path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('announcement/', views.announcement, name='announcement'),
    path('free_wifi/', views.free_wifi, name='free_wifi'),
    path('events/', views.events, name='events'),
    path('contact/', views.contact, name='contact'),
    path('hotspots/', views.hotspot_list, name='hotspot_list'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('viewing/', views.viewing, name='viewing'),
]
