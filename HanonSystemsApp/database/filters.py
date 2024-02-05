import django_filters

from .models import Program
from .models import Product
from .models import Test
from django import forms
from .forms import TestFilterForm


class ProgramFilter(django_filters.FilterSet):
    class Meta:
        model = Program
        fields = {'program_name' : [ "contains"], 'status' : [ "exact"], 'phase' : [ "exact"], 'enterproj_id' : [ "contains"], 'wbs_number' : [ "contains"], 'oem' : ["contains"]}

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = {'product_family' : [ "contains"], 'platform' : [ "contains"], 'communication_protocol' : [ "contains"], 'voltage' : [ "contains"], 'variant' : [ "contains"]}
        exclude = ['delete' ,]

class TestFilter(django_filters.FilterSet):
    targeted_start = django_filters.DateFilter(field_name='targeted_start',
                                           widget= forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
                                           lookup_expr='gte', label='Start Date')
    targeted_end = django_filters.DateFilter(field_name='targeted_end',
                                           widget= forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
                                           lookup_expr='lte', label='Start Date')
    setup_date = django_filters.DateFilter(field_name='setup_date',
                                           widget= forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
                                           lookup_expr='iexact', label='Start Date')
    class Meta:
        model = Test
        form = TestFilterForm
        exclude = ['delete' ,]
        fields = {'product_family' : [ "contains"], 'platform' : [ "contains"], 'communication_protocol' : [ "contains"], 'voltage' : [ "contains"], 'variant' : [ "contains"]}
