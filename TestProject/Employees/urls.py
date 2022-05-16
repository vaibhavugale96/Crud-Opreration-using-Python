import imp
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('vaibhav/', views.vaibhav, name="vaibhav"),
    path('register/', views.register, name="register")
    
  
    
]
