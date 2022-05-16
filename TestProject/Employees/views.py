
from unittest import result
from django import forms
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .forms import EmployeeForm
from .models import Designation

# Create your views here.

def vaibhav(request):
    template=loader.get_template('vaibhav.html')
    return HttpResponse(template.render())
def register(request):
    fm=EmployeeForm()
    return render(request,'register.html',{'form':fm})

def home(request):
    desgs=getDesignation(request)
    return render(request,'home.html',{'desgs':desgs})
    

def getDesignation(request):
    result = Designation.objects.all()
    return result

    