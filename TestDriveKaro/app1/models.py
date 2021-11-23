from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    Subject=models.CharField(max_length=100)
    contact=models.IntegerField(max_length=20)
    message=models.CharField(max_length=300)
    
    def __str__(self):
        return self.name


class filter_top(models.Model):
    TopBrands=models.CharField(max_length=50)
    color=models.CharField(max_length=30)
    Price=models.IntegerField(max_length=20)
    img=models.ImageField(upload_to="media/img" ,default="")
    def __str__(self):
        return self.TopBrands

class filter_luxury(models.Model):
    Luxury=models.CharField(max_length=50)
    color=models.CharField(max_length=30)
    Price=models.IntegerField(max_length=20)
    img=models.ImageField(upload_to="media/img" ,default="")
    def __str__(self):
        return self.Luxury
