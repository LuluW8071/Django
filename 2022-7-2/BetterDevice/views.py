from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,TemplateView,DeleteView,UpdateView,DetailView
from django.core.paginator import Paginator
from BetterDevice.models import Laptop
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.
from .forms import LaptopRegistration
@method_decorator(login_required(login_url = 'login'), name='dispatch')
class LaptopListView(ListView):
    model=Laptop
    template_name='BetterDevice/laptop-list.html'
    context_object_name='laptops'
    
    def get_context_data(self,*args ,**kwargs):
        laptops=self.get_queryset()#laptop is name of model
        paginator=Paginator(laptops,3)
        page_number=self.request.GET.get('page')
        page_obj=paginator.get_page(page_number)
        context={'laptops':page_obj}
        return context
    
@method_decorator(login_required(login_url = 'login'), name='dispatch')
class LaptopCreateView(CreateView):
    form_class=LaptopRegistration
    template_name='BetterDevice/laptop-create.html'
    success_url=reverse_lazy('laptop-list')
    
@method_decorator(login_required(login_url = 'login'), name='dispatch')
class LaptopUpdateView(UpdateView):
    model=Laptop
    template_name='BetterDevice/laptop-update.html'
    context_object_name='laptops'
    fields=['manufacture','name','ram','gpu','cpu','price']
    success_url=reverse_lazy('laptop-list')
    
@method_decorator(login_required(login_url = 'login'), name='dispatch')#this blocks unauthorized access
class LaptopDeleteView(DeleteView):
    model=Laptop
    template_name='BetterDevice/laptop-delete.html'
    success_url=reverse_lazy('laptop-list')