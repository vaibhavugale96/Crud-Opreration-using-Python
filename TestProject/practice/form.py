from cProfile import label
import email
from unicodedata import name
from django import forms

from .models import Student

# class StudentRegistration(forms.Form):
#     id=forms.CharField()
#     name=forms.CharField(required=False, label="Name",label_suffix=':')
#     clss=forms.CharField(required=False, label="Class",label_suffix=':')
#     sec=forms.CharField(required=False, label="Section",label_suffix=':')
#     city=forms.CharField(required=False, label="city",label_suffix=':')


class StudentRegistration(forms.ModelForm):
    class Meta:
        model =Student
        # fields=['empID','empName','empDesignation']
        fields='__all__'
        
