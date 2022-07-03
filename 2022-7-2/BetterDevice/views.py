
from django.views.generic import ListView,TemplateView,DeleteView,UpdateView,DetailView,CreateView
from django.core.paginator import Paginator
from BetterDevice.models import Laptop
from .forms import LaptopRegistration
from django.urls import reverse_lazy

# Create your views here.

class LaptopListView(ListView):
    model=Laptop
    template_name='BetterDevice/laptop-list.html'
    context_object_name='laptops'

    def get_context_data(self,*args,**kwargs):
        laptops=self.get_queryset()
        paginator=Paginator(laptops,5)
        page_number=self.request.GET.get('page')
        page_obj=paginator.get_page(page_number)
        context={'laptops':page_obj}
        return context
    
class LaptopCreateView(CreateView):
    form_class=LaptopRegistration
    template_name= 'BetterDevice/laptop-create.html'
    success_url=reverse_lazy('laptop-list')
    
class LaptopUpdateView(UpdateView):
    model=Laptop
    template_name= 'BetterDevice/laptop-update.html'
    context_object_name= 'laptops'
    fields= ('manufacture','name','price','ram','cpu')
    success_url= reverse_lazy('laptop-list')
    
class LaptopDeleteView(DeleteView):
    model=Laptop
    template_name='BetterDevice/laptop-delete.html'
    success_url= reverse_lazy('laptop-list')