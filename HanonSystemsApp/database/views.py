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
from datetime import timedelta
from django.utils import timezone
from django.http import HttpResponse
from django.db.models import Q
import math


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
    program_hours = {}
    
    all_logs = ChamberLog.objects.filter(timestamp__gte = dates[0]).filter(timestamp__lte = dates[1])    #getting all logs in the specified time period
    chambers = Chamber.objects.all()
    for chamber in chambers:
        chamber_name = chamber.chamber_name
        max_hours = chamber.max_daily_hours  #getting the max hour of the current chamber
        operable_hours = (dates[1]-dates[0]).days*max_hours #getting total time in period
        chamber_logs = all_logs.filter(chamber_id = chamber.chamber_id)        #getting logs of current chamber

        tests_checked= []       #to skip over tests that have already been accounted
        used_hours = {}     #to keep track of the operable hours used for a certain day
        
        program_hours[chamber_name] = {}
        
        for test in chamber_logs:
            if test.log_id.test_id in tests_checked:            #only assessing distinct tests
                continue
            else:
                tests_checked.append(test.log_id.test_id)
                
            test_logs = chamber_logs.filter(log_id__test_id= test.log_id.test_id).order_by("timestamp")       #getting chamber logs that belong to current test
            program_name = test.log_id.test_id.program_id.program_name
            
            stop = False
            logs = test_logs.filter(circuit_number = test_logs[0].circuit_number).order_by("timestamp")
            
            try:                #checking for log of test before the selected time period
                previous_log = ChamberLog.objects.filter(log_id__test_id= logs[0].log_id.test_id).filter(chamber_id= logs[0].chamber_id).filter(timestamp__lt = dates[0]).latest("timestamp")
            except:
                previous_log=0
            
            while stop == False:
                for log in logs:
                    if log == logs[0]:  #in case this is the leading log, check if the previous log's present
                        if previous_log == 0:           #case 1:first log of test
                            first_log = True
                            overlap = False
                        else:    
                            try:
                                last_log = ChamberLog.objects.filter(log_id__test_id= log.log_id.test_id).filter(chamber_id= log.chamber_id).filter(circuit_number = log.circuit_number).filter(timestamp__lt = log.timestamp).latest("timestamp")
                            except:
                                first_log = True               #case 2:no previous log in circuit, but there is a previous log from another circuit
                                switch_date = str(previous_log.timestamp.day) + "/" + str(previous_log.timestamp.month) + "/" + str(previous_log.timestamp.year)
                                try:                #checking used hours on the day of the previous log
                                    used = used_hours[switch_date]
                                except:
                                    used = 0 
                                time_adjustment = previous_log.timestamp - timedelta(0,(max_hours-used)*60*60)
                                in_between = (log.timestamp - time_adjustment).days*max_hours + (log.timestamp - time_adjustment).seconds/60/60
                                
                                if in_between >= log.total_hours:           #case 2.1: if running hours recorded overlaps the hours up until the previous log
                                    overlap = False
                                else:
                                    overlap = True
                                    no_overlap = log.timestamp - previous_log.timestamp      
                            else:                       #case 3: there is a previous log of the circuit, as well as a previous log that could belong to any circuit (these could be the same thing)
                                first_log = False  
                                if previous_log.timestamp > last_log.timestamp:     #checking to see if last log is before or after where we switched, if this is the first log of the time period, "try" makes sure that value 0 doesn't cause errors
                                    overlap = True              #case 3.1: there is overlap between these two logs
                                    no_overlap = log.timestamp - previous_log.timestamp
                                    switch_date = str(previous_log.timestamp.day) + "/" + str(previous_log.timestamp.month) + "/" + str(previous_log.timestamp.year)
                                    try:
                                        used = used_hours[switch_date]
                                    except:
                                        used = 0
                                else:                           #case 3.2: there is no overlap between these two logs
                                    overlap = False     
                                previous_log = last_log                        #make the previous log the one we searched for, indicate that there is a log before current one.
                                
                                
                    
                    if first_log == True:           #Case 1 and 2's:
                        date = str(log.timestamp.day) + "/" + str(log.timestamp.month) + "/" + str(log.timestamp.year)
                        if overlap == False:
                            running_hours = log.total_hours                         #Step 1: calculating hours
                            try:
                                status_hours = math.ceil(in_between - running_hours)
                            except:
                                status_hours = 0
                        else:         #Case 2's:
                            running_hours = math.ceil(in_between)
                            status_hours = 0
                            overlap = False
                            
                        if running_hours < max_hours:                           #updating used hours
                            used_hours[date] = running_hours
                        else:
                            used_hours[date] = max_hours        

                        
                        if program_name not in program_hours[chamber_name].keys():                                #Step 2: updating program hours, for logs that lead a series of logs
                            program_hours[chamber_name][program_name]={}
                            program_hours[chamber_name][program_name]["running"] = running_hours 
                            program_hours[chamber_name][program_name]["stopped"] = status_hours
                            program_hours[chamber_name][program_name]["operable"] = operable_hours
                            program_hours[chamber_name][program_name]["billing category"] = chamber.billing_category
                        else:               #program has been registered
                            program_hours[chamber_name][program_name]["running"] = program_hours[chamber_name][program_name]["running"] + running_hours
                            program_hours[chamber_name][program_name]["stopped"] = program_hours[chamber_name][program_name]["stopped"] + status_hours
                        
                        first_log= False
                        previous_log = log
                        #print("first log in new series:")
                        #print(program_hours)
                        
                        
                        if log.status == "stopped" or log == logs[len(logs)-1]:        #when the current log is the last of the circuit logs, or the stretch of logs is stopped.
                            try:
                                next_log = test_logs.filter(timestamp__gt = log.timestamp).earliest("timestamp")
                            except:
                                stop = True
                                break
                            else:
                                logs = test_logs.filter(timestamp__gt = log.timestamp).filter(circuit_number = next_log.circuit_number).order_by("timestamp")
                                break
                        continue
                    
                    
                    else:                                                                   #Case 3's:                  
                        running_hours = log.total_hours - previous_log.total_hours          #Step 1: calculating hours between two subsequent logs
                        current_timestamp = log.timestamp
                        previous_timestamp = previous_log.timestamp
                        date = str(current_timestamp.day) + "/" + str(current_timestamp.month) + "/" + str(current_timestamp.year)
                        previous_date = str(previous_timestamp.day) + "/" + str(previous_timestamp.month) + "/" + str(previous_timestamp.year) 
                        
                        if date == previous_date:                                                       #Case 1: when two subsequent logs are on the same day
                            in_between = (current_timestamp - previous_timestamp).seconds/60/60     #only time to be accounted for is that between two logs
                            try:
                                available = max_hours - used_hours[date]            #checking operable hours available
                            except:
                                available = max_hours
                                
                            if available > in_between:
                                status_hours = math.ceil(in_between - running_hours)
                            else:
                                status_hours = available - running_hours
                                
                            if status_hours < 0:                    #in case the assumption of max daily hours is incorrect, this prevents subtractions from previously summed status hours
                                status_hours = 0
                                
                            if date in used_hours:
                                if previous_log.status == "running" or previous_log.status == "stopped":
                                    used_hours[date] = used_hours[date] + running_hours
                                else:
                                    used_hours[date] = used_hours[date] + running_hours + status_hours
                            else:
                                if previous_log.status == "running" or previous_log.status == "stopped":
                                    used_hours[date] = running_hours
                                else:
                                    used_hours[date] = running_hours + status_hours
                                    
                            
                                  
                        else:                                                       #Case 2: when two subsequent logs are on different dates
                            endofday_previous = datetime(previous_timestamp.year, previous_timestamp.month, previous_timestamp.day, 23, 59, 59, 0)
                            startofday_current = datetime(current_timestamp.year, current_timestamp.month, current_timestamp.day, 0, 0, 0, 0)
                            beginning_period = (endofday_previous - previous_timestamp).seconds/60/60
                            in_between = (startofday_current - endofday_previous).days*max_hours
                            end_period = (current_timestamp - startofday_current).seconds/60/60
                            try:
                                available = max_hours - used_hours[previous_date]
                            except:
                                available = max_hours
                                
                            if available > beginning_period:                #adding duration of first period
                                occupied_beginning = beginning_period
                            else:
                                occupied_beginning = available
                            
                            if max_hours > end_period:                      #adding duration of end period
                                occupied_end = end_period 
                            else:
                                occupied_end = max_hours
                                                                         
                            status_hours = math.ceil(occupied_beginning + in_between +occupied_end - running_hours)         #adding duration of in between period

                            if status_hours < 0:                    #in case the assumption of max daily hours is incorrect, this prevents subtractions from previously summed status hours
                                status_hours = 0

                            if occupied_beginning + in_between < running_hours:                                             #updating used hours
                                if previous_log.status == "running":                                                    #Case 1: chamber run time can stretch from last log into the day of current log
                                    used_hours[date] = math.ceil(running_hours - occupied_beginning - in_between)
                                else:
                                    used_hours[date] = occupied_end
                            else:                                                                       #Case 2: chamber run time doesn't stretch from last log into the day of current log
                                if previous_log.status == "running":
                                    used_hours[date] = 0
                                elif previous_log.status == "stopped":
                                    if running_hours < occupied_end:
                                        used_hours[date] = running_hours
                                    else:
                                        used_hours[date] = occupied_end
                                else:
                                    used_hours[date] = occupied_end
                                    
                            
                            
                        if overlap == True:
                            grey_period = no_overlap.days*max_hours + no_overlap.seconds/60/60 - used
                            if running_hours >= grey_period:
                                running_hours = math.ceil(grey_period)
                                status_hours = 0
                            else:
                                status_hours = math.ceil(grey_period-running_hours)
                            overlap == False
                                

                    if program_name not in program_hours[chamber_name].keys():                                #Step 2: updating program hours
                        program_hours[chamber_name][program_name]={}
                        program_hours[chamber_name][program_name]["running"] = running_hours
                        program_hours[chamber_name][program_name]["stopped"] = 0
                        program_hours[chamber_name][program_name]["operable "] = operable_hours
                        program_hours[chamber_name][program_name]["billing category"] = chamber.billing_category
                        if previous_log.status == "running":
                            program_hours[chamber_name][program_name]["stopped"] = program_hours[chamber_name][program_name]["stopped"] + status_hours
                        else:
                            program_hours[chamber_name][program_name][previous_log.status] = status_hours 

                    else:                                                                   
                        program_hours[chamber_name][program_name]["running"] = program_hours[chamber_name][program_name]["running"] + running_hours
                        if previous_log.status not in program_hours[chamber_name][program_name].keys():
                            program_hours[chamber_name][program_name][previous_log.status] = status_hours
                        else:
                            if previous_log.status == "running":
                                program_hours[chamber_name][program_name]["stopped"] = program_hours[chamber_name][program_name]["stopped"] + status_hours
                            else:
                                program_hours[chamber_name][program_name][previous_log.status] = program_hours[chamber_name][program_name][previous_log.status] + status_hours                             
                            
                    previous_log = log
                    #print(program_hours)
                    
                    if log.status == "stopped" or log == logs[len(logs)-1]:        #Step 3: Checking switching conditions
                        try:
                            next_log = test_logs.filter(timestamp__gt = log.timestamp).earliest("timestamp")
                        except:
                            stop = True
                            break
                        else:
                            logs = test_logs.filter(timestamp__gt = log.timestamp).filter(circuit_number = next_log.circuit_number).order_by("timestamp")
                            break
    #print(program_hours)              
    #write csv file for program hours:
    a = open("database/static/database/programhours.csv", "w")
    a.write("")
    a.close()
    a = open("database/static/database/programhours.csv", "a")
    a.write("Chamber;Program;Running;Setup;Waiting for product;Stopped;Total Operable Hours;Billing Category\n")
    for i in program_hours:
        for x in program_hours[i]:
            a.write(f'{i};')
            a.write(f'{x};')
            try:
                a.write(f'{program_hours[i][x]["running"]};')
            except:
                a.write("0;")
            
            try: 
                a.write(f'{program_hours[i][x]["setup"]};')
            except:
                a.write("0;")
            
            try:
                a.write(f'{program_hours[i][x]["waiting for product"]};')
            except:
                a.write("0;")
            
            try:
                a.write(f'{program_hours[i][x]["stopped"]};')
            except:
                a.write("0;")

            a.write(f'{program_hours[i][x]["operable"]};')    
            a.write(f'{program_hours[i][x]["billing category"]}\n')

    a.close()  
    return HttpResponse("hours compiled");

def hours_download(request):
    return render(request, "html/hours_download.html")

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

def dut_history(request, id):
    test_list = Test_DUT.objects.filter(dut_id = id).order_by("test_id__targeted_start")
    test_history = {}
    accumulated_hours = 0
    for test in test_list:
        try:
            latest_duration = ChamberLog.objects.filter(log_id__test_id = test.test_id).filter(circuit_number = test.circuit_number).latest("timestamp").total_hours
        except:
            latest_duration = 0
        accumulated_hours += latest_duration
        if test.test_id.test_type_id.test_name in test_history:
            test_history[test.test_id.test_type_id.test_name] = [latest_duration + test_history[test.test_id.test_type_id.test_name][0], accumulated_hours]
        else:
            test_history[test.test_id.test_type_id.test_name] = [latest_duration, accumulated_hours]
    
    return render(request, "html/dut_history.html", {"test_history": test_history, "dut_name":test_list[0].dut_id.dut_name})

def harness_history(request, id):
    test_list = Test_Harness.objects.filter(harness_id = id).order_by("test_id__targeted_start")
    test_history = {}
    accumulated_hours = 0
    for test in test_list:
        try:
            latest_duration = ChamberLog.objects.filter(log_id__test_id = test.test_id).filter(circuit_number = test.circuit_number).latest("timestamp").total_hours
        except:
            latest_duration = 0
        accumulated_hours += latest_duration
        if test.test_id.test_type_id.test_name in test_history:
            test_history[test.test_id.test_type_id.test_name] = [latest_duration + test_history[test.test_id.test_type_id.test_name][0], accumulated_hours]
        else:
            test_history[test.test_id.test_type_id.test_name] = [latest_duration, accumulated_hours]
    
    return render(request, "html/harness_history.html", {"test_history": test_history, "harness_name":test_list[0].harness_id.harness_name})