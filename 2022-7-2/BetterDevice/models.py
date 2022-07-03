from django.db import models

# Create your models here.
class Laptop(models.Model):
    manufacture=models.CharField(max_length=50,null=True,blank=True)
    name=models.CharField(max_length=20,null=True,blank=True)
    ram=models.CharField(max_length=20,null=True,blank=True)
    gpu=models.CharField(max_length=20,null=True,blank=True)
    cpu=models.CharField(max_length=20,null=True,blank=True)
    price=models.DecimalField(max_digits=50,decimal_places=2,null=True,blank=True)
    
    def __str__(self):#now the name of the laptop will be shown 
        return(self.name)