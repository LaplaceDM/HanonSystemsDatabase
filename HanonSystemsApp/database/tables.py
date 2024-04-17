import django_tables2 as tables
from .models import *
from django_tables2.utils import A
from django_tables2_column_shifter.tables import ColumnShiftTableBootstrap3


class ProgramTable(ColumnShiftTableBootstrap3):
    delete = tables.LinkColumn('delete_program',text='delete', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    },orderable = False)

    update = tables.LinkColumn('update_program',text='edit', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    }, orderable = False)

    clone = tables.LinkColumn('clone2',text='clone', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    }, orderable = False)

    class Meta:
        model = Program
        exclude = ("program_id", )

class ProductTable(ColumnShiftTableBootstrap3):
    delete = tables.LinkColumn('delete_product',text='delete', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    }, orderable = False)

    update = tables.LinkColumn('update_product',text='edit', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    }, orderable = False)

    clone = tables.LinkColumn('clone1',text='clone', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    }, orderable = False)

    class Meta:
        model = Product
        exclude = ("product_id", )

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

    log = tables.LinkColumn('find',text='log', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    }, orderable = False)
    

    class Meta:
        model = Test
        exclude = ("test_id", )
        order_by = "program_id", "-test_map_id", "created"

class ChamberLogInfoTable(ColumnShiftTableBootstrap3):
    delete = tables.LinkColumn('delete_ChamberLogInfo',text= 'delete', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    }, orderable = False)

    update = tables.LinkColumn('update_ChamberLogInfo',text='edit', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    }, orderable = False)

    clone = tables.LinkColumn('clone3',text='clone', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    }, orderable = False)

    id = tables.LinkColumn('ChamberLog', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    }, orderable = True)


    class Meta:
        model = ChamberLogInfo

class ChamberLogTable(ColumnShiftTableBootstrap3):
    delete = tables.LinkColumn('delete_ChamberLog',text='delete', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    }, orderable = False)


    clone = tables.LinkColumn('clone4',text='clone', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    }, orderable = False)

    class Meta:
        model = ChamberLog
        
class DUTTable(ColumnShiftTableBootstrap3):
    delete = tables.LinkColumn('delete_dut',text='delete', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    }, orderable = False)

    update = tables.LinkColumn('update_dut',text='edit', args=[A('pk')], attrs={
    'a': {'class': 'btn', 'target': '__blank'}
    }, orderable = False)
    
    dut_name = tables.LinkColumn('dut_info', args=[A('pk')], attrs={
    'a': {'class': 'btn', 'target': '__blank'}
    }, orderable = True)

    class Meta:
        model = DUT
        exclude = ("dut_id", )
        
class SubcomponentTable(ColumnShiftTableBootstrap3):
    delete = tables.LinkColumn('delete_subcomponent',text='delete', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    }, orderable = False)

    update = tables.LinkColumn('update_subcomponent',text='edit', args=[A('pk')], attrs={
    'a': {'class': 'btn', 'target': '__blank'}
    }, orderable = False)

    class Meta:
        model = Subcomponent
        exclude = ("component_id","dut_id" )