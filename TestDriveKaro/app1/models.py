from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    companyname=models.CharField(max_length=100)
    contact=models.IntegerField()
    message=models.CharField(max_length=300)