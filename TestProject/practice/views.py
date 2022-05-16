from tkinter.font import names
from unicodedata import name
from django.forms import model_to_dict
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from pkg_resources import register_namespace_handler
from .models import Student
from .form import StudentRegistration
# Create your views here.
# def home(request):
#     template=loader.get_template('home.html')
#     return HttpResponse(template.render())
def home(request):
    return getStudentInfo(request)
def index(request):
    template=loader.get_template('digikull/index.html')
    return HttpResponse(template.render())
def about(request):
    template=loader.get_template('about.html')
    return HttpResponse(template.render())
def product(request):
    template=loader.get_template('digikull/product.html')
    return HttpResponse(template.render())

def service1(request):
    template=loader.get_template('digikull/service1.html')
    return HttpResponse(template.render())
def service2(request):
    template=loader.get_template('digikull/service2.html')
    return HttpResponse(template.render())
def contact(request):
    template=loader.get_template('digikull/contact.html')
    return HttpResponse(template.render())
def success(request):
    template=loader.get_template('success.html')
    return HttpResponse(template.render())


def getStudentInfo(request):
    studs=Student.objects.all()
    names=Student.objects.values_list('studentName',flat=True)
    return render(request,"digikull/home.html",{"students":studs,'names':names})

def registration(request):
    # CSRF- Cross site request forgery token
    if(request.method=="POST"):
        formStuReg=StudentRegistration(request.POST)
        if(formStuReg.is_valid()):
            print(formStuReg.cleaned_data['name'])
            print("post sucees")
            id=formStuReg.cleaned_data['id']
            nme=formStuReg.cleaned_data['name']
            clss=formStuReg.cleaned_data['clss']
            sec=formStuReg.cleaned_data['sec']
            city=formStuReg.cleaned_data['city']
            
            st=Student(studentID=id,studentName=nme,studentClass=clss,studentSection=sec,studentCity=city)
            
            st.save()
            
            return HttpResponseRedirect('/')
    else:
        
        formStuReg= StudentRegistration(auto_id=True,label_suffix='')
    
    return render(request,"registration.html",{"form":formStuReg})
# def registration(request):
#     if(request.method=="POST"):
#         form=StudentRegistration(request.POST)
#         if(form.is_valid()):
#             form.save()
#             return HttpResponseRedirect('/home')
#     else:
#         form=StudentRegistration()       
#         return render(request,'digikull/studentDetails6.html',{'form':form})

def studentDetails(request):
    id=request.GET.get('data')
    student=Student.objects.get(studentID=id)
    if(request.method=='POST'):
        form=StudentRegistration(request.POST)
        if(form.is_valid()):
            form=StudentRegistration(request.POST,instance=student)
            form.save()
            return HttpResponseRedirect('/')
    else:
        print(model_to_dict(student))
        form=StudentRegistration(initial=model_to_dict(student))
        return render(request,'registration.html',{'form':form})

def deleteStuds(request):
    id=request.GET.get('data')
    student=Student.objects.filter(studentID=id)
    student.delete()
    return HttpResponseRedirect('/')