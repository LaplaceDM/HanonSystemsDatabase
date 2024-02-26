import django_filters

from .models import Program
from .models import Product
from .models import Test
from .models import ChamberLogInfo
from .models import ChamberLog
from django import forms


class ProgramFilter(django_filters.FilterSet):
    created = django_filters.DateFilter(field_name='created', 
                                            widget= forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
                                            lookup_expr='date',
                                            label='created')
    class Meta:
        model = Program
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