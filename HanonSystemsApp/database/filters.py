import django_filters

from .models import Program
from .models import Product
from .models import Test
from .models import ChamberLogInfo
from .models import ChamberLog
from .models import *
from .models import DAR
from .models import Chamber
from django import forms


class ProgramFilter(django_filters.FilterSet):
    created = django_filters.DateFilter(field_name='created', 
                                            widget= forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
                                            lookup_expr='date',
                                            label='created')
    class Meta:
        model = Program
        exclude = ['delete' ,]


class LaptopFilter(django_filters.FilterSet):
    class Meta:
        model = Laptop
        exclude = ['delete' ,]

class Test_HarnessFilter(django_filters.FilterSet):
    class Meta:
        model = Test_Harness
        exclude = ['delete' ,]
class Test_DUTFilter(django_filters.FilterSet):
    class Meta:
        model = Test_DUT
        exclude = ['delete' ,]

class Technician_SkillFilter(django_filters.FilterSet):
    class Meta:
        model = Technician_Skill
        exclude = ['delete' ,]


class TestMapFilter(django_filters.FilterSet):
    class Meta:
        model = TestMap
        exclude = ['delete' ,]


class Test_ChamberFilter(django_filters.FilterSet):
    class Meta:
        model = Test_Chamber
        exclude = ['delete' ,]

class Program_CageFilter(django_filters.FilterSet):
    class Meta:
        model = Program_Cage
        exclude = ['delete' ,]

class Program_DARFilter(django_filters.FilterSet):
    class Meta:
        model = Program_DAR
        exclude = ['delete' ,]

class Program_FluidFilter(django_filters.FilterSet):
    class Meta:
        model = Program_Fluid
        exclude = ['delete' ,]

class DARChannelFilter(django_filters.FilterSet):
    class Meta:
        model = DARChannel
        exclude = ['delete' ,]

class HarnessFilter(django_filters.FilterSet):
    class Meta:
        model = Harness
        exclude = ['delete' ,]

class SkillFilter(django_filters.FilterSet):
    class Meta:
        model = Skill
        exclude = ['delete' ,]

class LabFilter(django_filters.FilterSet):
    class Meta:
        model = Lab
        exclude = ['delete' ,]

class TestTypeFilter(django_filters.FilterSet):
    class Meta:
        model = TestType
        exclude = ['delete' ,]


class TechnicianFilter(django_filters.FilterSet):
    class Meta:
        model = Technician
        exclude = ['delete' ,]


class FluidFilter(django_filters.FilterSet):
    class Meta:
        model = Fluid
        exclude = ['delete' ,]

class CageFilter(django_filters.FilterSet):
    class Meta:
        model = Cage
        exclude = ['delete' ,]

class DarFilter(django_filters.FilterSet):
    class Meta:
        model = DAR
        exclude = ['delete' ,]

class ChamberFilter(django_filters.FilterSet):
    class Meta:
        model = Chamber
        exclude = ['delete' ,]

class ProductFilter(django_filters.FilterSet):
    created = django_filters.DateFilter(field_name='created', 
                                            widget= forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
                                            lookup_expr='date',
                                            label='created')
    class Meta:
        model = Product
        exclude = ['delete' ,]

class TestFilter(django_filters.FilterSet):
        targeted_start = django_filters.DateFilter(field_name='targeted_start', 
                                            widget= forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
                                            lookup_expr='gte', label='Targed Start')
        targeted_end = django_filters.DateFilter(field_name='targeted_end',
                                            widget= forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
                                            lookup_expr='lte', label='Targed End')
        setup_date = django_filters.DateFilter(field_name='setup_date', 
                                            widget= forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
                                            lookup_expr='iexact', label='Start Date')
        created = django_filters.DateFilter(field_name='Created', 
                                            widget= forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
                                            lookup_expr='date',
                                            label='Created')
        class Meta:
            model = Test
            exclude = ['delete' ,]

class ChamberLogInfoFilter(django_filters.FilterSet):
    created = django_filters.DateFilter(field_name='created', 
                                            widget= forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
                                            lookup_expr='date',
                                            label='created')
    class Meta:
        model = ChamberLogInfo
        exclude = ['delete' ,]
        
class ChamberLogFilter(django_filters.FilterSet):
    timestamp = django_filters.DateFilter(field_name='timestamp', 
                                            widget= forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
                                            lookup_expr='date',
                                            label='timestamp')
    class Meta:
        model = ChamberLog
        exclude = ['delete' ,]
        
class DUTFilter(django_filters.FilterSet):
    received_date = django_filters.DateFilter(field_name='received_date', 
                                            widget= forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
                                            lookup_expr='date',
                                            label='received date')
    storage_date = django_filters.DateFilter(field_name='storage_date', 
                                            widget= forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
                                            lookup_expr='date',
                                            label='storage date')
    class Meta:
        model = DUT
        exclude = ['delete' ,]
        
class DAR_ChannelFilter(django_filters.FilterSet):
    class Meta:
        model = DARChannel
        exclude = ['channel_id' ,]