from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
   
    path('digikull/',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('digikull/product/',views.product,name="product"),
    path('studentDetails/',views.studentDetails,name="studentDetails"),
    path('deleteStuds/',views.deleteStuds,name="deleteStuds"),
    path('digikull/service1/',views.service1,name="service1"),
    path('digikull/service2/',views.service2,name="service2"),
    path('digikull/contact/',views.contact,name="contact"),
    path('registration/',views.registration,name="registration")
    
]
