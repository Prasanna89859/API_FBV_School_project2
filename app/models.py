from django.db import models

# Create your models here.

class School(models.Model):
    Sname=models.CharField(max_length=100)
    Spricipal=models.CharField(max_length=100)
    Slocation=models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.Sname
    
