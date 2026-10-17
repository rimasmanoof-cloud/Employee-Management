from django.db import models

# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    department=models.CharField(max_length=50)
    salary=models.IntegerField()
    joining_date=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    