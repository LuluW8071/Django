from django.shortcuts import render

from polls.models import Laptops

# Create your views here.
def index(request):
    laptop_list=Laptops.objects.all()
    laptops={
        'laptops':laptop_list
    }
    
    return render(request, 'polls/laptop-list.html',laptops)