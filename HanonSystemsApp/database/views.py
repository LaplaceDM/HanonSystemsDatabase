from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView 
from .models import *
from django.shortcuts import render
from django_filters.views import FilterView
from .filters import ProgramFilter
from .filters import ProductFilter
from .filters import TestFilter
from .filters import ChamberLogInfoFilter
from .filters import ChamberLogFilter
from .filters import CageFilter
from .filters import ChamberFilter
from .filters import *
from django_tables2.views import SingleTableMixin
from .tables import ProgramTable
from .tables import ProductTable
from .tables import TestTable
from .tables import TestMapTable
from .tables import ChamberLogTable
from .tables import ChamberLogInfoTable
from .tables import CageTable
from .tables import ChamberTable
from .tables import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ProgramForm
from .forms import *
from .forms import TestForm
from .forms import ChamberLogInfoForm
from .forms import ChamberLogForm
from .forms import TestUpdateForm
from .forms import CageForm
from .forms import ChamberForm
from .forms import DarForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django_tables2 import MultiTableMixin
from django.views.generic.base import TemplateView
from django.views.generic.detail import SingleObjectMixin

from django.utils import timezone
from django.http import HttpResponse
from django.db.models import Q


class LaptopListView(SingleTableMixin,  CreateView, FilterView):

    model = Laptop
    table_class = LaptopTable
    template_name = 'html/index.html'
    paginate_by = 20
    filterset_class = LaptopFilter
    form_class = LaptopForm
    success_url = '/database/Laptop'

    def form_invalid(self, form):
        messages.error(self.request, 'sorry error')
        return HttpResponseRedirect(reverse("Laptop"))

class UpdateTableViewLaptop(SingleTableMixin,  UpdateView):
    
    model = Laptop
    table_class = LaptopTable
    form_class = LaptopForm
    template_name = 'html/update.html'
    success_url = '/database/Laptop'



def delete_Laptop(request, pk):

    Laptop.objects.filter(laptop_id=pk).delete()

    return HttpResponseRedirect(reverse("Laptop"))


class Test_HarnessListView(SingleTableMixin,  CreateView, FilterView):

    model = Test_Harness
    table_class = Test_HarnessTable
    template_name = 'html/index.html'
    paginate_by = 20
    filterset_class = Test_HarnessFilter
    form_class = Test_HarnessForm
    success_url = '/database/Test_Harness'

    def form_invalid(self, form):
        messages.error(self.request, 'sorry error')
        return HttpResponseRedirect(reverse("Test_Harness"))

class UpdateTableViewTest_Harness(SingleTableMixin,  UpdateView):
    
    model = Test_Harness
    table_class = Test_HarnessTable
    form_class = Test_HarnessForm
    template_name = 'html/update.html'
    success_url = '/database/Test_Harness'



def delete_Test_Harness(request, pk):

    Test_Harness.objects.filter(id=pk).delete()

    return HttpResponseRedirect(reverse("Test_Harness"))


class Technician_SkillListView(SingleTableMixin,  CreateView, FilterView):

    model = Technician_Skill
    table_class = Technician_SkillTable
    template_name = 'html/index.html'
    paginate_by = 20
    filterset_class = Technician_SkillFilter
    form_class = Technician_SkillForm
    success_url = '/database/Technician_Skill'

    def form_invalid(self, form):
        messages.error(self.request, 'sorry error')
        return HttpResponseRedirect(reverse("Technician_Skill"))

class UpdateTableViewTechnician_Skill(SingleTableMixin,  UpdateView):
    
    model = Technician_Skill
    table_class = Technician_SkillTable
    form_class = Technician_SkillForm
    template_name = 'html/update.html'
    success_url = '/database/Technician_Skill'



def delete_Technician_Skill(request, pk):

    Technician_Skill.objects.filter(id=pk).delete()

    return HttpResponseRedirect(reverse("Technician_Skill"))


class TestMapListView(SingleTableMixin,  CreateView, FilterView):

    model = TestMap
    table_class = TestMapTable
    template_name = 'html/index.html'
    paginate_by = 20
    filterset_class = TestMapFilter
    form_class = TestMapForm
    success_url = '/database/TestMap'

    def form_invalid(self, form):
        messages.error(self.request, 'sorry error')
        return HttpResponseRedirect(reverse("TestMap"))

class UpdateTableViewTestMap(SingleTableMixin,  UpdateView):
    
    model = TestMap
    table_class = TestMapTable
    form_class = TestMapForm
    template_name = 'html/update.html'
    success_url = '/database/TestMap'



def delete_TestMap(request, pk):

    TestMap.objects.filter(test_map_id=pk).delete()

    return HttpResponseRedirect(reverse("TestMap"))



class DAR_LaptopListView(SingleTableMixin,  CreateView, FilterView):

    model = DAR_Laptop
    table_class = DAR_LaptopTable
    template_name = 'html/index.html'
    paginate_by = 20
    filterset_class = DAR_LaptopFilter
    form_class = DAR_LaptopForm
    success_url = '/database/DAR_Laptop'

    def form_invalid(self, form):
        messages.error(self.request, 'sorry error')
        return HttpResponseRedirect(reverse("DAR_Laptop"))

class UpdateTableViewDAR_Laptop(SingleTableMixin,  UpdateView):
    
    model = DAR_Laptop
    table_class = DAR_LaptopTable
    form_class = DAR_LaptopForm
    template_name = 'html/update.html'
    success_url = '/database/DAR_Laptop'



def delete_DAR_Laptop(request, pk):

    DAR_Laptop.objects.filter(id=pk).delete()

    return HttpResponseRedirect(reverse("DAR_Laptop"))



class Test_ChamberListView(SingleTableMixin,  CreateView, FilterView):

    model = Test_Chamber
    table_class = Test_ChamberTable
    template_name = 'html/index.html'
    paginate_by = 20
    filterset_class = Test_ChamberFilter
    form_class = Test_ChamberForm
    success_url = '/database/Test_Chamber'

    def form_invalid(self, form):
        messages.error(self.request, 'sorry error')
        return HttpResponseRedirect(reverse("Test_Chamber"))

class UpdateTableViewTest_Chamber(SingleTableMixin,  UpdateView):
    
    model = Test_Chamber
    table_class = Test_ChamberTable
    form_class = Test_ChamberForm
    template_name = 'html/update.html'
    success_url = '/database/Test_Chamber'



def delete_Test_Chamber(request, pk):

    Test_Chamber.objects.filter(id=pk).delete()

    return HttpResponseRedirect(reverse("Test_Chamber"))



class Program_CageListView(SingleTableMixin,  CreateView, FilterView):

    model = Program_Cage
    table_class = Program_CageTable
    template_name = 'html/index.html'
    paginate_by = 20
    filterset_class = Program_CageFilter
    form_class = Program_CageForm
    success_url = '/database/Program_Cage'

    def form_invalid(self, form):
        messages.error(self.request, 'sorry error')
        return HttpResponseRedirect(reverse("Program_Cage"))

class UpdateTableViewProgram_Cage(SingleTableMixin,  UpdateView):
    
    model = Program_Cage
    table_class = Program_CageTable
    form_class = Program_CageForm
    template_name = 'html/update.html'
    success_url = '/database/Program_Cage'



def delete_Program_Cage(request, pk):

    Program_Cage.objects.filter(id=pk).delete()

    return HttpResponseRedirect(reverse("Program_Cage"))



class Program_DARListView(SingleTableMixin,  CreateView, FilterView):

    model = Program_DAR
    table_class = Program_DARTable
    template_name = 'html/index.html'
    paginate_by = 20
    filterset_class = Program_DARFilter
    form_class = Program_DARForm
    success_url = '/database/Program_DAR'

    def form_invalid(self, form):
        messages.error(self.request, 'sorry error')
        return HttpResponseRedirect(reverse("Program_DAR"))

class UpdateTableViewProgram_DAR(SingleTableMixin,  UpdateView):
    
    model = Program_DAR
    table_class = Program_DARTable
    form_class = Program_DARForm
    template_name = 'html/update.html'
    success_url = '/database/Program_DAR'



def delete_Program_DAR(request, pk):

    Program_DAR.objects.filter(id=pk).delete()

    return HttpResponseRedirect(reverse("Program_DAR"))


class Program_FluidListView(SingleTableMixin,  CreateView, FilterView):

    model = Program_Fluid
    table_class = Program_FluidTable
    template_name = 'html/index.html'
    paginate_by = 20
    filterset_class = Program_FluidFilter
    form_class = Program_FluidForm
    success_url = '/database/Program_Fluid'

    def form_invalid(self, form):
        messages.error(self.request, 'sorry error')
        return HttpResponseRedirect(reverse("Program_Fluid"))

class UpdateTableViewProgram_Fluid(SingleTableMixin,  UpdateView):
    
    model = Program_Fluid
    table_class = Program_FluidTable
    form_class = Program_FluidForm
    template_name = 'html/update.html'
    success_url = '/database/Program_Fluid'



def delete_Program_Fluid(request, pk):

    Program_Fluid.objects.filter(id=pk).delete()

    return HttpResponseRedirect(reverse("Program_Fluid"))





class DARChannelListView(SingleTableMixin,  CreateView, FilterView):

    model = DARChannel
    table_class = DARChannelTable
    template_name = 'html/index.html'
    paginate_by = 20
    filterset_class = DARChannelFilter
    form_class = DARChannelForm
    success_url = '/database/DARChannel'

    def form_invalid(self, form):
        messages.error(self.request, 'sorry error')
        return HttpResponseRedirect(reverse("DARChannel"))

class UpdateTableViewDARChannel(SingleTableMixin,  UpdateView):
    
    model = DARChannel
    table_class = DARChannelTable
    form_class = DARChannelForm
    template_name = 'html/update.html'
    success_url = '/database/DARChannel'



def delete_DARChannel(request, pk):

    DARChannel.objects.filter(channel_id=pk).delete()

    return HttpResponseRedirect(reverse("DARChannel"))



class FluidListView(SingleTableMixin,  CreateView, FilterView):

    model = Fluid
    table_class = FluidTable
    template_name = 'html/index.html'
    paginate_by = 20
    filterset_class = FluidFilter
    form_class = FluidForm
    success_url = '/database/Fluid'

    def form_invalid(self, form):
        messages.error(self.request, 'sorry error')
        return HttpResponseRedirect(reverse("Fluid"))

class UpdateTableViewFluid(SingleTableMixin,  UpdateView):
    
    model = Fluid
    table_class = FluidTable
    form_class = FluidForm
    template_name = 'html/update.html'
    success_url = '/database/Fluid'



def delete_Fluid(request, pk):

    Fluid.objects.filter(fluid_id=pk).delete()

    return HttpResponseRedirect(reverse("Fluid"))



class TechnicianListView(SingleTableMixin,  CreateView, FilterView):

    model = Technician
    table_class = TechnicianTable
    template_name = 'html/index.html'
    paginate_by = 20
    filterset_class = TechnicianFilter
    form_class = TechnicianForm
    success_url = '/database/Technician'

    def form_invalid(self, form):
        messages.error(self.request, 'sorry error')
        return HttpResponseRedirect(reverse("Technician"))

class UpdateTableViewTechnician(SingleTableMixin,  UpdateView):
    
    model = Technician
    table_class = TechnicianTable
    form_class = TechnicianForm
    template_name = 'html/update.html'
    success_url = '/database/Technician'



def delete_Technician(request, pk):

    Technician.objects.filter(technician_id=pk).delete()

    return HttpResponseRedirect(reverse("Technician"))


class TestTypeListView(SingleTableMixin,  CreateView, FilterView):

    model = TestType
    table_class = TestTypeTable
    template_name = 'html/index.html'
    paginate_by = 20
    filterset_class = TestTypeFilter
    form_class = TestTypeForm
    success_url = '/database/TestType'

    def form_invalid(self, form):
        messages.error(self.request, 'sorry error')
        return HttpResponseRedirect(reverse("TestType"))

class UpdateTableViewTestType(SingleTableMixin,  UpdateView):
    
    model = TestType
    table_class = TestTypeTable
    form_class = TestTypeForm
    template_name = 'html/update.html'
    success_url = '/database/TestType'



def delete_TestType(request, pk):

    TestType.objects.filter(test_type_id=pk).delete()

    return HttpResponseRedirect(reverse("TestType"))


class LabListView(SingleTableMixin,  CreateView, FilterView):

    model = Lab
    table_class = LabTable
    template_name = 'html/index.html'
    paginate_by = 20
    filterset_class = LabFilter
    form_class = LabForm
    success_url = '/database/Lab'

    def form_invalid(self, form):
        messages.error(self.request, 'sorry error')
        return HttpResponseRedirect(reverse("Lab"))

class UpdateTableViewLab(SingleTableMixin,  UpdateView):
    
    model = Lab
    table_class = LabTable
    form_class = LabForm
    template_name = 'html/update.html'
    success_url = '/database/Lab'



def delete_Lab(request, pk):

    Lab.objects.filter(lab_id=pk).delete()

    return HttpResponseRedirect(reverse("Lab"))


class SkillListView(SingleTableMixin,  CreateView, FilterView):

    model = Skill
    table_class = SkillTable
    template_name = 'html/index.html'
    paginate_by = 20
    filterset_class = SkillFilter
    form_class = SkillForm
    success_url = '/database/Skill'

    def form_invalid(self, form):
        messages.error(self.request, 'sorry error')
        return HttpResponseRedirect(reverse("Skill"))

class UpdateTableViewSkill(SingleTableMixin,  UpdateView):
    
    model = Skill
    table_class = SkillTable
    form_class = SkillForm
    template_name = 'html/update.html'
    success_url = '/database/Skill'



def delete_Skill(request, pk):

    Skill.objects.filter(skill_id=pk).delete()

    return HttpResponseRedirect(reverse("Skill"))

class HarnessListView(SingleTableMixin,  CreateView, FilterView):

    model = Harness
    table_class = HarnessTable
    template_name = 'html/index.html'
    paginate_by = 20
    filterset_class = HarnessFilter
    form_class = HarnessForm
    success_url = '/database/Harness'

    def form_invalid(self, form):
        messages.error(self.request, 'sorry error')
        return HttpResponseRedirect(reverse("Harness"))

class UpdateTableViewHarness(SingleTableMixin,  UpdateView):
    
    model = Harness
    table_class = HarnessTable
    form_class = HarnessForm
    template_name = 'html/update.html'
    success_url = '/database/Harness'



def delete_Harness(request, pk):

    Harness.objects.filter(harness_id=pk).delete()

    return HttpResponseRedirect(reverse("Harness"))















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
    

class CageListView(SingleTableMixin,  CreateView, FilterView):

    model = Cage
    table_class = CageTable
    template_name = 'html/cage.html'
    paginate_by = 20
    filterset_class = CageFilter
    form_class = CageForm
    success_url = '/database/cage'

    def form_invalid(self, form):
        messages.error(self.request, 'sorry error')
        return HttpResponseRedirect(reverse("cage"))
    
class UpdateTableViewCage(SingleTableMixin,  UpdateView):
    
    model = Cage
    table_class = CageTable
    form_class = CageForm
    template_name = 'html/update cage.html'
    success_url = '/database/cage'



def delete_cage(request, pk):

    Cage.objects.filter(cage_id=pk).delete()

    return HttpResponseRedirect(reverse("cage"))
    


class ChamberListView(SingleTableMixin,  CreateView, FilterView):

    model = Chamber
    table_class = ChamberTable
    template_name = 'html/Chamber.html'
    paginate_by = 20
    filterset_class = ChamberFilter
    form_class = ChamberForm
    success_url = '/database/Chamber'

    def form_invalid(self, form):
        messages.error(self.request, 'sorry error')
        return HttpResponseRedirect(reverse("Chamber"))
    
class UpdateTableViewChamber(SingleTableMixin,  UpdateView):
    
    model = Chamber
    table_class = ChamberTable
    form_class = ChamberForm
    template_name = 'html/update Chamber.html'
    success_url = '/database/Chamber'



def delete_Chamber(request, pk):

    Chamber.objects.filter(chamber_id=pk).delete()

    return HttpResponseRedirect(reverse("Chamber"))




class UpdateTableViewProgram(SingleTableMixin,  UpdateView):
    
    model = Program
    table_class = ProgramTable
    form_class = ProgramForm
    template_name = 'html/update.html'
    success_url = '/database/program'



def delete_program(request, pk):

    Program.objects.filter(program_id=pk).delete()

    return HttpResponseRedirect(reverse("program"))


class DarListView(SingleTableMixin,  CreateView, FilterView):

    model = DAR
    table_class = DarTable
    template_name = 'html/Dar.html'
    paginate_by = 20
    filterset_class = DarFilter
    form_class = DarForm
    success_url = '/database/Dar'

    def form_invalid(self, form):
        messages.error(self.request, 'sorry error')
        return HttpResponseRedirect(reverse("Dar"))
    
class UpdateTableViewDar(SingleTableMixin,  UpdateView):
    
    model = DAR
    table_class = DarTable
    form_class = DarForm
    template_name = 'html/update Dar.html'
    success_url = '/database/Dar'



def delete_Dar(request, pk):

    DAR.objects.filter(dar_id=pk).delete()

    return HttpResponseRedirect(reverse("Dar"))
    



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
    table_class = ProductTable
    form_class = ProductForm
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

class UpdateTableViewTest(SingleTableMixin,  UpdateView, FilterView):
    
    
    model = Test
    table_class = TestTable
    template_name = 'html/update_test.html'
    form_class = TestUpdateForm
    # template_name_suffix = 'html/index.html'
    # fields = '__all__'
    filterset_class = TestFilter
    success_url = '/database/tests'

def find(request, pk):
    p = ChamberLogInfo.objects.get(test_id = pk).pk
    return HttpResponseRedirect(reverse("ChamberLog", kwargs={'pk': p}))


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
    ch = ChamberLogInfo(chamber_id = obj.chamber_id, program_id = obj.program_id, technician_id = obj.technician_id, test_id = Test.objects.get(pk = obj.pk),
                                pretest_inspection_and_photo=None,
                                setup_photo=None,
                                humidity=None,
                                system_pressure=None,
                                voltage=None,
                                system_restriction_target=None,
                                system_restriction_record=None,
                                trial_run_record_and_process=None,
                                special_requirements=None)

    ch.save()

    return HttpResponseRedirect(reverse("test"))



def clone_item1(request, pk):

    obj = Product.objects.get(product_id = pk)
    obj.pk = None
    obj.created = timezone.now()
    obj.save()

    return HttpResponseRedirect(reverse("product"))

def clone_item2(request, pk):

    obj = Program.objects.get(program_id = pk)
    obj.pk = None
    obj.created = timezone.now()
    obj.save()
    

    return HttpResponseRedirect(reverse("program"))



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
    
def children1(request):
    print(2232323232323232323)
    test_type_id = request.body
    try:
        test_type_id = int(test_type_id)
    except:
        a = open("database/templates/html/children", "w")
        a.write("{\n")
        a.close()
        return HttpResponse()
    else:
        test_cham = Test.objects.filter(test_id = test_type_id) #.order_by("targeted_start");
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
    chamber_id = request.body
    try:
        chamber_id = int(chamber_id)
    except:
        a = open("database/templates/html/chamber_schedule", "w")
        a.write("")
        a.close()
        return HttpResponse("No chamber selected")
    else:
        chamber_tests = Test.objects.filter(Q(scheduling = "current")|Q(scheduling = "upcoming")).filter(chamber_id = chamber_id).order_by("targeted_start")
        a = open("database/templates/html/chamber_schedule", "w")
        a.write("{\n")
        a.close()
       

        a = open("database/templates/html/chamber_schedule", "a")
        for i in range(len(chamber_tests)):
            a.write(f'\"booking{i}\": {{\"targeted_start\" : \"{chamber_tests[i].targeted_start}\", \"targeted_end\" : \"{chamber_tests[i].targeted_end}\",' 
                    + f'\"test_map_id\" : \"{chamber_tests[i].test_map_id.tr}\", \"product_id\" : \"{chamber_tests[i].product_id}\", \"test_type_id\" : \"{chamber_tests[i].test_type_id}\", \"program_id\" : '
                    + f'\"{chamber_tests[i].program_id}\", \"scheduling\" : \"{chamber_tests[i].scheduling}\"}},\n')
        
        a.write(f'\"chamber\": \"{Chamber.objects.get(chamber_id=chamber_id)}\"\n}}')
        a.close()
        return HttpResponse("Chamber schedule compiled")

def get_chamber_schedule(request):
    return render(request, "html/chamber_schedule")

def dar_schedule(request):
    dar_id = request.body
    try:
        dar_id = int(dar_id)
    except:
        a = open("database/templates/html/dar_schedule", "w")
        a.write("")
        a.close()
        return HttpResponse("No DAR selected")
    else:
        dar_tests = Test.objects.filter(Q(scheduling = "current")|Q(scheduling = "upcoming")).filter(dar_id = dar_id).order_by("targeted_start")
        a = open("database/templates/html/dar_schedule", "w")
        a.write("{\n")
        a.close()

        a = open("database/templates/html/dar_schedule", "a")
        for i in range(len(dar_tests)):
            a.write(f'\"booking{i}\": {{\"targeted_start\" : \"{dar_tests[i].targeted_start}\", \"targeted_end\" : \"{dar_tests[i].targeted_end}\",' 
                    + f'\"test_map_id\" : \"{dar_tests[i].test_map_id.tr}\", \"product_id\" : \"{dar_tests[i].product_id}\", \"test_type_id\" : \"{dar_tests[i].test_type_id}\", \"program_id\" : '
                    + f'\"{dar_tests[i].program_id}\", \"scheduling\" : \"{dar_tests[i].scheduling}\"}},\n')
        
        a.write(f'\"DAR\": \"{DAR.objects.get(dar_id=dar_id)}\"\n}}')
        a.close()
        return HttpResponse("DAR schedule compiled")

def get_dar_schedule(request):
    return render(request, "html/dar_schedule")

def cage_schedule(request):
    cage_id = request.body
    try:
        cage_id = int(cage_id)
    except:
        a = open("database/templates/html/cage_schedule", "w")
        a.write("")
        a.close()
        return HttpResponse("No cage selected")
    else:
        cage_tests = Test.objects.filter(Q(scheduling = "current")|Q(scheduling = "upcoming")).filter(cage_id = cage_id).order_by("targeted_start")
        a = open("database/templates/html/cage_schedule", "w")
        a.write("{\n")
        a.close()

        a = open("database/templates/html/cage_schedule", "a")
        for i in range(len(cage_tests)):
            a.write(f'\"booking{i}\": {{\"targeted_start\" : \"{cage_tests[i].targeted_start}\", \"targeted_end\" : \"{cage_tests[i].targeted_end}\",' 
                    + f'\"test_map_id\" : \"{cage_tests[i].test_map_id.tr}\", \"product_id\" : \"{cage_tests[i].product_id}\", \"test_type_id\" : \"{cage_tests[i].test_type_id}\", \"program_id\" : '
                    + f'\"{cage_tests[i].program_id}\", \"scheduling\" : \"{cage_tests[i].scheduling}\"}},\n')
        
        a.write(f'\"Cage\": \"{Cage.objects.get(cage_id=cage_id)}\"\n}}')
        a.close()
        return HttpResponse("Cage schedule compiled")

def get_cage_schedule(request):
    return render(request, "html/cage_schedule")



class ChamberLogInfoListView(SingleTableMixin, CreateView, FilterView):
    
    model = ChamberLogInfo
    table_class = ChamberLogInfoTable
    template_name = 'html/ChamberLogInfo.html'
    paginate_by = 20
    success_url = '/database/ChamberLogInfo'
    filterset_class = ChamberLogInfoFilter
    form_class = ChamberLogInfoForm

    

class UpdateTableViewChamberLogInfo(SingleTableMixin,  UpdateView):
    
    
    model = ChamberLogInfo
    table_class = ChamberLogInfoTable
    template_name = 'html/update_ChamberLogInfo.html'
    form_class = ChamberLogInfoForm
    # template_name_suffix = 'html/index.html'
    # fields = '__all__'
    success_url = '/database/ChamberLogInfo'



def delete_item_ChamberLogInfo(request, pk):

    ChamberLogInfo.objects.filter(id=pk).delete()

    items = ChamberLogInfo.objects.all()

    context = {
    'items': items
    }

    return HttpResponseRedirect(reverse("ChamberLogInfo"))

def clone_item3(request, pk):

    obj = ChamberLogInfo.objects.get(id = pk)
    obj.pk = None
    obj.created = timezone.now()
    obj.save()

    return HttpResponseRedirect(reverse("ChamberLogInfo"))

class ChamberLogView(SingleTableMixin, CreateView, FilterView):
    template_name = 'html/ChamberLog.html'
    model = ChamberLog
    table_class = ChamberLogTable
    form_class = ChamberLogForm
    filterset_class = ChamberLogFilter
    
    def get_queryset(self, *args, **kwargs):
        return ChamberLog.objects.filter(log_id = self.kwargs.get('pk'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ChamberLogInfo'] = ChamberLogInfo.objects.filter(pk = self.kwargs.get('pk'))
        return context
    
    def get_success_url(self):
        return reverse('ChamberLog', kwargs={'pk': self.kwargs.get('pk')})
    
    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, 'sorry error')
        return HttpResponseRedirect(reverse("ChamberLog", kwargs={'pk': self.kwargs.get('pk')}))

def delete_item_ChamberLog(request, pk):
    item = ChamberLog.objects.get(id = pk).log_id.id

    ChamberLog.objects.filter(id=pk).delete()

   

    return HttpResponseRedirect(reverse("ChamberLog", kwargs={'pk': item}))

def clone_item4(request, pk):

    obj = ChamberLog.objects.get(id = pk)
    obj.pk = None
    obj.save()

    return  HttpResponseRedirect(reverse('ChamberLog', kwargs={'pk': obj.log_id.id}))

    """
    table_pagination = {
        "per_page": 10
    }
    """

class ProgramInfoView(MultiTableMixin, TemplateView):
    template_name = "html/Temp4.html"
    def get_tables(self, **kwargs):
        qs = TestMap.objects.filter(program_id = self.kwargs.get('pk'))
        qs2 = Test.objects.filter(program_id = self.kwargs.get('pk'))
        qs3 = Product.objects.filter(program_id = self.kwargs.get('pk'))
        self.tables = [
            TestMapTable(qs),
            TestTable(qs2),
            ProductTable(qs3)
        ]
        return super().get_tables()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Program'] = Program.objects.filter(pk = self.kwargs.get('pk'))
        return context

def menu(request):
    return render(request, "html/menu.html")



def short(request):
    program_id = request.body
    try:
        program_id = int(program_id)
    except:
        a = open("database/templates/html/short", "w")
        a.write("{\n")
        a.close()
        return HttpResponse()
    else:
        prod = Product.objects.filter(program_id = program_id) #.order_by("targeted_start");
        map = TestMap.objects.filter(program_id = program_id)
        a = open("database/templates/html/short", "w")
        a.write("{\n")
        a.close()
        a = open("database/templates/html/short", "a")
        b = 0
        for i in range(len(prod)):
            b = b+1
            a.write(f'\"id{i}\": {{\"product_id\" : \"{prod[i].product_id}\"}}')
            if i != (len(prod)-1):
                a.write(",\n")
        if (len(prod) > 0 and len(map) > 0):
            a.write(",\n")
        for i in range(len(map)):
            a.write(f'\"id{b}\": {{\"test_map_id\" : \"{map[i].test_map_id}\"}}')
            b = b + 1
            if i != (len(map)-1):
                a.write(",\n")
        a.write("\n}")
        a.close()
        return HttpResponse("program shortlist compiled")
    
def getshort(request):
    return render(request, "html/short")