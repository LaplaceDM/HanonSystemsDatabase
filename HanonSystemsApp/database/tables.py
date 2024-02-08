import django_tables2 as tables
from .models import Program
from .models import Product
from .models import Test
from django_tables2.utils import A
from django_tables2_column_shifter.tables import ColumnShiftTableBootstrap3


class ProgramTable(ColumnShiftTableBootstrap3):
    delete = tables.LinkColumn('delete_program',text='delete', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    },orderable = False)

    update = tables.LinkColumn('update_program',text='edit', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    }, orderable = False)

    class Meta:
        model = Program

class ProductTable(ColumnShiftTableBootstrap3):
    delete = tables.LinkColumn('delete_product',text='delete', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    }, orderable = False)

    update = tables.LinkColumn('update_product',text='edit', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    }, orderable = False)

    class Meta:
        model = Product

class TestTable(ColumnShiftTableBootstrap3):
    delete = tables.LinkColumn('delete_test',text='delete', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    }, orderable = False)

    update = tables.LinkColumn('update_test',text='edit', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    }, orderable = False)

    clone = tables.LinkColumn('clone',text='clone', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    }, orderable = False)


    class Meta:
        model = Test
        #template_name = "django_tables2/bootstrap5.html"
        exclude = ("test_id", )