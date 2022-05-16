from email.policy import default
from pyexpat import model
from statistics import mode
from unicodedata import name
from django.db import models

# Create your models here.
class Designation(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
     return self.name

class Employee(models.Model):
    empID=models.IntegerField(primary_key=True)
    empName=models.CharField(max_length=70)
    empDesignation=models.ForeignKey(Designation,default=1,on_delete=models.CASCADE)