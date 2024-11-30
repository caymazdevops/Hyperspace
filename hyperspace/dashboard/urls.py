from django.urls import path
from django.conf import settings
from . import views 



urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('sporpage', views.sporpage, name='sporpage'),
    
]