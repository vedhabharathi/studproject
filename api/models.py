from django.db import models

class Students(models.Model):
    Rollno=models.IntegerField()
    Name=models.CharField(max_length=64)
    Class=models.IntegerField()
    Gender=models.CharField(max_length=64)
    Age=models.IntegerField()
    Group=models.CharField(max_length=64)
    Address=models.CharField(max_length=256)

    def __str__(self):
        return self.name