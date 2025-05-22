from django.urls import path
from  . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('announcement/', views.announcement, name='announcement'),
    path('free_wifi/', views.free_wifi, name='free_wifi'),
    path('events/', views.events, name='events'),
    path('contact/', views.contact, name='contact'),
    path('hotspots/', views.hotspot_list, name='hotspot_list'),
   
    
    
]
