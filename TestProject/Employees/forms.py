from cProfile import label
from dataclasses import fields
from pyexpat import model
from tkinter import Widget
from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model =Employee
        # fields=['empID','empName','empDesignation']
        fields='__all__'
        labels={'empID':'Enter Employee Id','empName':'Enter Employee Name','empDesignation':'Enter Designation'}
        widgets={'empID':forms.NumberInput(attrs={'class':'empID'})}
