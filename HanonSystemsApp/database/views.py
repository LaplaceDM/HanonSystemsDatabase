from django.views.generic import ListView 
from .models import Program
from .models import Product
from django.shortcuts import render
from django_filters.views import FilterView
from .filters import ProgramFilter
from .filters import ProductFilter
from django_tables2.views import SingleTableMixin
from .tables import ProgramTable
from .tables import ProductTable
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ProgramForm
from .forms import ProductForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView


class ProgramListView(SingleTableMixin,  CreateView, FilterView):
    
    
    model = Program
    table_class = ProgramTable
    template_name = 'html/index.html'
    paginate_by = 20
    filterset_class = ProgramFilter
    form_class = ProgramForm
    success_url = '/database/'

    def form_invalid(self, form):
        messages.error(self.request, 'sorry error')
        return HttpResponseRedirect(reverse("index"))

class UpdateTableView(SingleTableMixin,  UpdateView):
    
    
    model = Program
    template_name = 'html/update.html'
    # form_class = ProgramForm
    # template_name_suffix = 'html/index.html'
    fields = '__all__'
    success_url = '/database/'



def delete_item(request, pk):

    Program.objects.filter(program_id=pk).delete()

    items = Program.objects.all()

    context = {
    'items': items
    }

    return HttpResponseRedirect(reverse("index"))



class ProductListView(SingleTableMixin,  CreateView, FilterView):
    
    
    model = Product
    table_class = ProductTable
    template_name = 'html/product.html'
    paginate_by = 20
    filterset_class = ProductFilter
    form_class = ProductForm
    success_url = '/database/product'

    def form_invalid(self, form):
        messages.error(self.request, 'sorry error')
        return HttpResponseRedirect(reverse("product"))

class UpdateTableViewProduct(SingleTableMixin,  UpdateView):
    
    
    model = Product
    template_name = 'html/update_prod.html'
    # form_class = ProductForm
    # template_name_suffix = 'html/index.html'
    fields = '__all__'
    success_url = '/database/product'



def delete_item_product(request, pk):

    Product.objects.filter(product_id=pk).delete()

    items = Product.objects.all()

    context = {
    'items': items
    }

    return HttpResponseRedirect(reverse("product"))



            
