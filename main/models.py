from django.db import models

# Create your models here.

class Students(models.Model):
   name = models.CharField(max_length=50)
   major = models.CharField(max_length=50)
   number = models.CharField(max_length=50)
   year = models.CharField(max_length=50)
   level = models.CharField(max_length=50)
   average = models.CharField(max_length=50)
   
   def __str__(self):
   		return self.name
