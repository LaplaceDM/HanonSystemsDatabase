import django_filters

from .models import Program
from .models import Product


class ProgramFilter(django_filters.FilterSet):
    class Meta:
        model = Program
        fields = {'program_name' : [ "contains"], 'status' : [ "exact"], 'phase' : [ "exact"], 'enterproj_id' : [ "contains"], 'wbs_number' : [ "contains"], 'oem' : ["contains"]}

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = {'product_family' : [ "contains"], 'platform' : [ "contains"], 'communication_protocol' : [ "contains"], 'voltage' : [ "contains"], 'variant' : [ "contains"]}