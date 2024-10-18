from django.urls import path
from app import views  # Import the views module

urlpatterns = [
    path('', views.home, name='home'),  
]
