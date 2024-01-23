import django_tables2 as tables
from .models import Program
from .models import Product
from django_tables2.utils import A

class ProgramTable(tables.Table):
    delete = tables.LinkColumn('delete_item',text='delete', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    }, orderable = False)

    update = tables.LinkColumn('update',text='update', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    }, orderable = False)

    class Meta:
        model = Program
        #template_name = "django_tables2/bootstrap5.html"
        exclude = ("program_id", )

class ProductTable(tables.Table):
    delete = tables.LinkColumn('delete_product',text='delete', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    }, orderable = False)

    update = tables.LinkColumn('update_product',text='update', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    }, orderable = False)

    class Meta:
        model = Product
        #template_name = "django_tables2/bootstrap5.html"
        exclude = ("product_id", )