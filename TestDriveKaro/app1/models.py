import math
from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    Subject=models.CharField(max_length=100)
    contact=models.IntegerField()
    message=models.CharField(max_length=300)
    
    def __str__(self):
        return self.name


class filter_top(models.Model):
    TopBrands=models.CharField(max_length=50)
    model=models.CharField(max_length=50,default="")
    color=models.CharField(max_length=30)
    Price=models.IntegerField()
    img=models.ImageField(upload_to="media/img" ,default="")
    url=models.URLField(max_length=200,default="")
    def __str__(self):
        return self.model

class filter_luxury(models.Model):
    Luxury=models.CharField(max_length=50)
    model=models.CharField(max_length=50,default="")
    color=models.CharField(max_length=30)
    Price=models.IntegerField()
    img=models.ImageField(upload_to="media/img" ,default="")
    url=models.URLField(max_length=200,default="")

    def __str__(self):
        return self.model

class brand_top(models.Model):
    name=models.CharField(max_length=50)
    logo=models.ImageField(upload_to="media/top/logo" ,default="")

    def __str__(self):
        return self.name

class brand_luxury (models.Model):
    name=models.CharField(max_length=50)
    logo=models.ImageField(upload_to="media/luxury/logo" ,default="")

    def __str__(self):
        return self.name

class cars(models.Model):
    brand = models.CharField(max_length=150)
    model = models.CharField(max_length=150)
    price = models.CharField(max_length=50)
    img1 = models.ImageField(upload_to="media/carinfo",default="")
    img2 = models.ImageField(upload_to="media/carinfo",default="")
    img3 = models.ImageField(upload_to="media/carinfo",default="")
    img4 = models.ImageField(upload_to="media/carinfo",default="")
    body_type= models.CharField(max_length=150)
    mileage= models.CharField(max_length=150)
    fuel_type= models.CharField(max_length=150)
    transmission= models.CharField(max_length=150)
    sitting = models.CharField(max_length=150)
    sunroof = models.CharField(max_length=150)
    tank_capicity= models.CharField(max_length=150)

