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
from django_tables2.views import SingleTableMixin
from .tables import ProgramTable
from .tables import ProductTable
from .tables import TestTable
from .tables import ChamberLogTable
from .tables import ChamberLogInfoTable
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ProgramForm
from .forms import ProductForm
from .forms import TestForm
from .forms import ChamberLogInfoForm
from .forms import ChamberLogForm
from .forms import TestUpdateForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django_tables2 import MultiTableMixin
from django.views.generic.base import TemplateView
from django.views.generic.detail import SingleObjectMixin
from datetime import datetime
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
    table_class = ProgramTable
    form_class = ProgramForm
    template_name = 'html/update.html'
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


def menu(request):
    return render(request, "html/menu.html")

def hours_calculations(request):
    return render(request, "html/hours_calculations.html")

def calculate(request):
    dates = str(request.body)
    first = dates.find("'")
    last = dates.find("'", first +1)
    dates = dates[first+1: last]
    dates = dates.split(",")
    dates[0] = datetime.strptime(dates[0], "%Y-%m-%d")                  #converting date string to date object
    dates[1] = datetime.strptime(dates[1], "%Y-%m-%d")
    print(dates)
    program_hours = {}
    equipment_hours = {}

    all_logs = ChamberLog.objects.filter(timestamp__gte = dates[0]).filter(timestamp__lte = dates[1])    #getting all logs in the specified time period
    print(all_logs)
    chambers = Chamber.objects.all()
    for chamber in chambers:
        chamber_name = chamber.chamber_name
        max_hours = chamber.max_daily_hours  #getting the max hour of the current chamber
        total_hours = (dates[1]-dates[0]).days*max_hours #getting total time in period
        chamber_logs = all_logs.filter(log_id__test_id__chamber_id = chamber.chamber_id)        #getting logs of current chamber
        tests = chamber_logs.distinct("log_id__test_id")        #getting tests that ran in that chamber
        equipment_hours[chamber_name]["hours assessed"] = total_hours
        equipment_hours[chamber_name]["running"]=0

        for test in tests:
            test_logs = chamber_logs.filter(log_id__test_id= test.test_id).order_by("timestamp")       #getting chamber logs that belong to current test
            program_name = test.program_id.program_name
            
            stop = False
            logs = test_logs.filter(circuit_number = test_logs[0].circuit_number).order_by("timestamp")
            
            while stop == False:
                for log in logs:
                    if log == logs[0]:  #in case this is the first of a stretch of logs
                        if ChamberLog.objects.filter(log_id__test_id= log.test_id).filter(log_id__test_id__chamber_id= log.test_id.chamber_id).filter(timestamp__lt = log.timestamp).filter(circuit_number = log.circuit_number).latest("timestamp").status != "stopped":
                            previous_log = ChamberLog.objects.filter(log_id__test_id= log.test_id).filter(log_id__test_id__chamber_id= log.test_id.chamber_id).filter(timestamp__lt = log.timestamp).filter(circuit_number = log.circuit_number).latest("timestamp")
                        else:
                            previous_log= log
                            continue
                    
                    running_hours = log.running_hours - previous_log.running_hours
                    current_timestamp = datetime.strptime(log.timestamp, "%Y-%m-%d %H:%M:%-S")
                    previous_timestamp = datetime.strptime(previous_log.timestamp, "%Y-%m-%d %H:%M:%-S")
                    status_hours = (current_timestamp-previous_timestamp).days*max_hours - running_hours
                    previous_log = log

                    if program_name not in program_hours.keys():                                #updating program hours
                        program_hours[program_name]["running"] = running_hours
                        program_hours[program_name][previous_log.status] = status_hours

                    else:
                        program_hours[program_name]["running"] = program_hours[program_name]["running"] + running_hours
                        if previous_log.status not in program_hours[program_name].keys():
                            program_hours[program_name][previous_log.status] = status_hours
                        else:
                            program_hours[program_name][previous_log.status] = program_hours[program_name][previous_log.status] + status_hours                             

                
                    equipment_hours[chamber_name]["running"]=equipment_hours[chamber_name]["running"] + running_hours           #updating equipment hours
                    if previous_log.status not in equipment_hours[chamber_name].keys():
                        equipment_hours[chamber_name][previous_log.status] = status_hours
                    else:
                        equipment_hours[chamber_name][previous_log.status] = [chamber_name][previous_log.status] + status_hours
                    
                    
                    if log.status == "stopped"| log == logs[len(logs)-1]:        #when the current log is the last of the circuit logs, or the stretch of logs is stopped.
                        next_log = ChamberLog.objects.filter(log_id__test_id= log.test_id).filter(log_id__test_id__chamber_id= log.test_id.chamber_id).filter(timestamp__gte = log.timestamp).exclude(status = "stopped").earliest("timestamp")
                        if next_log:
                            logs = ChamberLog.objects.filter(log_id__test_id= log.test_id).filter(log_id__test_id__chamber_id= log.test_id.chamber_id).filter(timestamp__gte = log.timestamp).filter(circuit_number = next_log.circuit_number).order_by("timestamp")
                            break
                        else:
                            stop = True
                            break
                        
                        
    #write csv file for program hours:
    a = open("database/static/database/programhours.csv", "w")
    a.write("")
    a.close()
    a = open("database/static/database/programhours.csv", "a")
    a.write("Program;Running;Setup;Waiting for product;Stopped\n")
    for i in program_hours:
        a.write(f'{i};')
        if i["running"]:
            a.write(f'{i["running"]};')
        else:
            a.write("0;")
        if i["set up"]:
            a.write(f'{i["set up"]};')
        else:
            a.write("0;")
        if i["waiting for product"]:
            a.write(f'{i["waiting for product"]};')
        else:
            a.write("0;")
        if i["stopped"]:
            a.write(f'{i["stopped"]}\n')
        else:
            a.write("0\n")
    a.close()
    
    #write csv file for equipment hours:
    a = open("database/static/database/equipmenthours.csv", "w")
    a.write("")
    a.close()
    a = open("database/static/database/equipmenthours.csv", "a")
    a.write("Chamber;Total time assessed;Running;Setup;Waiting for product;Stopped\n")
    for i in program_hours:
        a.write(f'{i};{i[total_hours]};')
        if i["running"]:
            a.write(f'{i["running"]};')
        else:
            a.write("0;")
        if i["set up"]:
            a.write(f'{i["set up"]};')
        else:
            a.write("0;")
        if i["waiting for product"]:
            a.write(f'{i["waiting for product"]};')
        else:
            a.write("0;")
        if i["stopped"]:
            a.write(f'{i["stopped"]}\n')
        else:
            a.write("0\n")
    a.close()
               
    return HttpResponse("hours compiled");

def dut_hours(request):
    dut = int(request.body)
    test_hours = {}
    tests = ChamberLog.objects.filter(dut_id = dut).distinct("test_id")
    for test in tests:
        total_hours = ChamberLog.objects.filter(log_id__test_id = test.log_id.test_id).filter(dut_id = dut).latest("timestamp").total_hours
        test_hours[test.log_id.test_id.test_type_id.test_name] = total_hours
    
    a = open("database/templates/html/dut_hours", "w")
    a.write("")
    a.close()
    a = open("database/templates/html/dut_hours", "a")
    a.write("{{")
    
    for i in test_hours:
        a.write( f'\"{i}\": {test_hours[i]},\n')
    a.write("}}")
    a.close()
    
    return HttpResponse("dut hours compiled")