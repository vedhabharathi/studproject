from django.db import models
class Student(models.Model):
    Rollno=models.IntegerField()
    Name=models.CharField(max_length=64)
    Class=models.IntegerField()
    Gender=models.CharField(max_length=64)
    Age=models.IntegerField()
    Group=models.CharField(max_length=64)
    Address=models.CharField(max_length=256)
    

