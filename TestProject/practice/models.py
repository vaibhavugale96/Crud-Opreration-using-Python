from statistics import mode
from django.db import models

# Create your models here.
class Student(models.Model):
    studentID=models.IntegerField()
    studentName=models.CharField(max_length=60)
    studentClass=models.CharField(max_length=20)
    studentSection=models.CharField(max_length=20)
    studentCity=models.CharField(max_length=20)
