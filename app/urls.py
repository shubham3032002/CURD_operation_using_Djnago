from django.urls import path
from app import views  # Import the views module

urlpatterns = [
    path('', views.home, name='home'),
    path("insert",views.insertData,name="InsertData"),
    path("update/<id>",views.UpdateData,name="UpdateData"),
    path("delete/<id>",views.DeleteData,name="DeleteData"),
]
