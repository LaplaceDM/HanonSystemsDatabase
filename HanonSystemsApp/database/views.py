from django.views.generic import ListView 
from .models import Program
from .models import Product
from .models import Test
from .models import Test_Chamber
from .models import Program_DAR
from .models import Program_Cage
from django.shortcuts import render
from django_filters.views import FilterView
from .filters import ProgramFilter
from .filters import ProductFilter
from .filters import TestFilter
from django_tables2.views import SingleTableMixin
from .tables import ProgramTable
from .tables import ProductTable
from .tables import TestTable
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ProgramForm
from .forms import ProductForm
from .forms import TestForm
from .forms import TestFilterForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django_tables2 import MultiTableMixin
from django.views.generic.base import TemplateView

from django.utils import timezone
from django.http import HttpResponse
from django.db.models import Q


class ProgramListView(SingleTableMixin,  CreateView, FilterView):

    model = Program
    table_class = ProgramTable
    template_name = 'html/index.html'
    paginate_by = 20
    filterset_class = ProgramFilter
    form_class = ProgramForm
    success_url = '/database/program'

    def form_invalid(self, form):
        messages.error(self.request, 'sorry error')
        return HttpResponseRedirect(reverse("program"))

class UpdateTableViewProgram(SingleTableMixin,  UpdateView):
    
    model = Program
    template_name = 'html/update.html'
    fields = '__all__'
    success_url = '/database/program'



def delete_program(request, pk):

    Program.objects.filter(program_id=pk).delete()

    return HttpResponseRedirect(reverse("program"))



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
    fields = '__all__'
    success_url = '/database/product'



def delete_item_product(request, pk):

    Product.objects.filter(product_id=pk).delete()

    return HttpResponseRedirect(reverse("product"))

class TestListView(SingleTableMixin, CreateView, FilterView):
    
    model = Test
    table_class = TestTable
    template_name = 'html/test.html'
    paginate_by = 20
    success_url = '/database/tests'
    filterset_class = TestFilter
    form_class = TestForm

    """
    filterset_class = ProductFilter
    form_class = ProductForm
    success_url = '/database/product'
    

    def form_invalid(self, form):
        messages.error(self.request, 'sorry error')
        """
class UpdateTableViewTest(SingleTableMixin,  UpdateView):
    
    
    model = Test
    table_class = TestTable
    template_name = 'html/update_prod.html'
    form_class = TestForm
    # template_name_suffix = 'html/index.html'
    # fields = '__all__'
    success_url = '/database/tests'



def delete_item_test(request, pk):

    Test.objects.filter(test_id=pk).delete()

    items = Test.objects.all()

    context = {
    'items': items
    }

    return HttpResponseRedirect(reverse("test"))

def clone_item(request, pk):

    obj = Test.objects.get(test_id = pk)
    obj.pk = None
    obj.created = timezone.now()
    obj.save()

    return HttpResponseRedirect(reverse("test"))



def children(request):
    test_type_id = request.body
    try:
        test_type_id = int(test_type_id)
    except:
        a = open("database/templates/html/children", "w")
        a.write("{\n")
        a.close()
        return HttpResponse()
    else:
        test_cham = Test_Chamber.objects.filter(test_type_id = test_type_id) #.order_by("targeted_start");
        a = open("database/templates/html/children", "w")
        a.write("{\n")
        a.close()
        a = open("database/templates/html/children", "a")
        for i in range(len(test_cham)):
            a.write(f'\"id{i}\": {{\"chamber_id\" : \"{test_cham[i].chamber_id.chamber_id}\"}}')
            if i != (len(test_cham)-1):
                a.write(",\n")
        a.write("\n}")
        a.close()
        return HttpResponse("product highligth compiled")
    
def getchildren(request):
    return render(request, "html/children")


def darchildren(request):
    program_id = request.body
    try:
        program_id = int(program_id)
    except:
        a = open("database/templates/html/children", "w")
        a.write("{\n")
        a.close()
        return HttpResponse()
    else:
        prog_dar = Program_DAR.objects.filter(program_id = program_id) #.order_by("targeted_start");
        prog_cage = Program_Cage.objects.filter(program_id = program_id)
        a = open("database/templates/html/children", "w")
        a.write("{\n")
        a.close()
        a = open("database/templates/html/children", "a")
        b = 0
        for i in range(len(prog_dar)):
            b = b+1
            a.write(f'\"id{i}\": {{\"dar_id\" : \"{prog_dar[i].dar_id.dar_id}\"}}')
            if i != (len(prog_dar)-1):
                a.write(",\n")
        if (len(prog_dar) > 0 and len(prog_cage) > 0):
            a.write(",\n")
        for i in range(len(prog_cage)):
            a.write(f'\"id{b}\": {{\"cage_id\" : \"{prog_cage[i].cage_id.cage_id}\"}}')
            b = b + 1
            if i != (len(prog_cage)-1):
                a.write(",\n")
        a.write("\n}")
        a.close()
        return HttpResponse("product highligth compiled")
    
def getdarchildren(request):
    return render(request, "html/children")
"""
class TestTablesView(MultiTableMixin, TemplateView):
    items = Test.objects.all()
    items2 = Product.objects.all()
    template_name = 'html/index.html'
    tables = [
        TestTable(items),
        ProductTable(items2)
    ]

    table_pagination = {
        "per_page": 10
    }
"""

def chamber_schedule(request):
    chamber_id = request.body;
    try:
        chamber_id = int(chamber_id);
    except:
        a = open("database/templates/html/chamber_schedule", "w");
        a.write("");
        a.close();
        return HttpResponse("No chamber selected")
    else:
        chamber_tests = Test.objects.filter(Q(scheduling = "current")|Q(scheduling = "upcoming")).filter(chamber_id = chamber_id).order_by("targeted_start");
        a = open("database/templates/html/chamber_schedule", "w");
        a.write("{\n");
        a.close();

        a = open("database/templates/html/chamber_schedule", "a");
        for i in range(len(chamber_tests)):
            a.write(f'\"booking{i}\": {{\"targeted_start\" : \"{chamber_tests[i].targeted_start}\", \"targeted_end\" : \"{chamber_tests[i].targeted_end}\",' 
                    + f'\"test_map_id\" : \"{chamber_tests[i].test_map_id.tr}\", \"test_type_id\" : \"{chamber_tests[i].test_type_id}\", \"program_id\" : '
                    + f'\"{chamber_tests[i].program_id}\", \"scheduling\" : \"{chamber_tests[i].scheduling}\"}}');
            if i != (len(chamber_tests)-1):
                a.write(",\n")
        a.write("\n}");
        a.close();
        return HttpResponse("Chamber schedule compiled");

def get_chamber_schedule(request):
    return render(request, "html/chamber_schedule");

def dar_schedule(request):
    dar_id = request.body;
    try:
        dar_id = int(dar_id);
    except:
        a = open("database/templates/html/dar_schedule", "w");
        a.write("");
        a.close();
        return HttpResponse("No DAR selected")
    else:
        dar_tests = Test.objects.filter(Q(scheduling = "current")|Q(scheduling = "upcoming")).filter(dar_id = dar_id).order_by("targeted_start");
        a = open("database/templates/html/dar_schedule", "w");
        a.write("{\n");
        a.close();

        a = open("database/templates/html/dar_schedule", "a");
        for i in range(len(dar_tests)):
            a.write(f'\"booking{i}\": {{\"targeted_start\" : \"{dar_tests[i].targeted_start}\", \"targeted_end\" : \"{dar_tests[i].targeted_end}\",' 
                    + f'\"test_map_id\" : \"{dar_tests[i].test_map_id.tr}\", \"test_type_id\" : \"{dar_tests[i].test_type_id}\", \"program_id\" : '
                    + f'\"{dar_tests[i].program_id}\", \"scheduling\" : \"{dar_tests[i].scheduling}\"}}');
            if i != (len(dar_tests)-1):
                a.write(",\n")
        a.write("\n}");
        a.close();
        return HttpResponse("DAR schedule compiled");

def get_dar_schedule(request):
    return render(request, "html/dar_schedule");

def cage_schedule(request):
    cage_id = request.body;
    try:
        cage_id = int(cage_id);
    except:
        a = open("database/templates/html/cage_schedule", "w");
        a.write("");
        a.close();
        return HttpResponse("No cage selected");
    else:
        cage_tests = Test.objects.filter(Q(scheduling = "current")|Q(scheduling = "upcoming")).filter(cage_id = cage_id).order_by("targeted_start");
        a = open("database/templates/html/cage_schedule", "w");
        a.write("{\n");
        a.close();

        a = open("database/templates/html/cage_schedule", "a");
        for i in range(len(cage_tests)):
            a.write(f'\"booking{i}\": {{\"targeted_start\" : \"{cage_tests[i].targeted_start}\", \"targeted_end\" : \"{cage_tests[i].targeted_end}\",' 
                    + f'\"test_map_id\" : \"{cage_tests[i].test_map_id.tr}\", \"test_type_id\" : \"{cage_tests[i].test_type_id}\", \"program_id\" : '
                    + f'\"{cage_tests[i].program_id}\", \"scheduling\" : \"{cage_tests[i].scheduling}\"}}');
            if i != (len(cage_tests)-1):
                a.write(",\n")
        a.write("\n}");
        a.close();
        return HttpResponse("Cage schedule compiled");

def get_cage_schedule(request):
    return render(request, "html/cage_schedule");