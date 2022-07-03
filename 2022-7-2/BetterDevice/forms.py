from django.core import validators 
from django import forms 
from .models import Laptop

class LaptopRegistration(forms.ModelForm):
    class Meta:
        model = Laptop
        fields= ['manufacture','name','price','ram','cpu']