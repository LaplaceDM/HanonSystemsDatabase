import django_tables2 as tables
from .models import *
from django_tables2.utils import A
from django_tables2_column_shifter.tables import ColumnShiftTableBootstrap3



class LaptopTable(ColumnShiftTableBootstrap3):
    delete = tables.LinkColumn('delete_Laptop',text='delete', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    },orderable = False)

    update = tables.LinkColumn('update_Laptop',text='edit', args=[A('pk')], attrs={
    'a': {'class': 'btn', 'target': '_blank'}
    }, orderable = False)

    class Meta:
        model = Laptop
        exclude = ("laptop_id", )

class Test_HarnessTable(ColumnShiftTableBootstrap3):
    delete = tables.LinkColumn('delete_Test_Harness',text='delete', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    },orderable = False)

    update = tables.LinkColumn('update_Test_Harness',text='edit', args=[A('pk')], attrs={
    'a': {'class': 'btn', 'target': '_blank'}
    }, orderable = False)

    class Meta:
        model = Test_Harness
        exclude = ("id", )

class Test_DUTTable(ColumnShiftTableBootstrap3):
    delete = tables.LinkColumn('delete_Test_DUT',text='delete', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    },orderable = False)

    update = tables.LinkColumn('update_Test_DUT',text='edit', args=[A('pk')], attrs={
    'a': {'class': 'btn', 'target': '_blank'}
    }, orderable = False)

    class Meta:
        model = Test_DUT
        exclude = ("id", )

class Technician_SkillTable(ColumnShiftTableBootstrap3):
    delete = tables.LinkColumn('delete_Technician_Skill',text='delete', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    },orderable = False)

    update = tables.LinkColumn('update_Technician_Skill',text='edit', args=[A('pk')], attrs={
    'a': {'class': 'btn', 'target': '_blank'}
    }, orderable = False)

    class Meta:
        model = Technician_Skill
        exclude = ("id", )


class TestMapTable(ColumnShiftTableBootstrap3):
    delete = tables.LinkColumn('delete_TestMap',text='delete', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    },orderable = False)

    update = tables.LinkColumn('update_TestMap',text='edit', args=[A('pk')], attrs={
    'a': {'class': 'btn', 'target': '_blank'}
    }, orderable = False)

    class Meta:
        model = TestMap
        exclude = ("test_map_id", )



class Test_ChamberTable(ColumnShiftTableBootstrap3):
    delete = tables.LinkColumn('delete_Test_Chamber',text='delete', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    },orderable = False)

    update = tables.LinkColumn('update_Test_Chamber',text='edit', args=[A('pk')], attrs={
    'a': {'class': 'btn', 'target': '_blank'}
    }, orderable = False)

    class Meta:
        model = Test_Chamber
        exclude = ("Test_Chamber_id", )


class Program_CageTable(ColumnShiftTableBootstrap3):
    delete = tables.LinkColumn('delete_Program_Cage',text='delete', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    },orderable = False)

    update = tables.LinkColumn('update_Program_Cage',text='edit', args=[A('pk')], attrs={
    'a': {'class': 'btn', 'target': '_blank'}
    }, orderable = False)

    class Meta:
        model = Program_Cage
        exclude = ("id", )


class Program_DARTable(ColumnShiftTableBootstrap3):
    delete = tables.LinkColumn('delete_Program_DAR',text='delete', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    },orderable = False)

    update = tables.LinkColumn('update_Program_DAR',text='edit', args=[A('pk')], attrs={
    'a': {'class': 'btn', 'target': '_blank'}
    }, orderable = False)

    class Meta:
        model = Program_DAR
        exclude = ("id", )

class Program_FluidTable(ColumnShiftTableBootstrap3):
    delete = tables.LinkColumn('delete_Program_Fluid',text='delete', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    },orderable = False)

    update = tables.LinkColumn('update_Program_Fluid',text='edit', args=[A('pk')], attrs={
    'a': {'class': 'btn', 'target': '_blank'}
    }, orderable = False)

    class Meta:
        model = Program_Fluid
        exclude = ("id", )

class DARChannelTable(ColumnShiftTableBootstrap3):
    delete = tables.LinkColumn('delete_DARChannel',text='delete', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    },orderable = False)

    update = tables.LinkColumn('update_DARChannel',text='edit', args=[A('pk')], attrs={
    'a': {'class': 'btn', 'target': '_blank'}
    }, orderable = False)

    class Meta:
        model = DARChannel
        exclude = ("channel_id", )

class HarnessTable(ColumnShiftTableBootstrap3):
    delete = tables.LinkColumn('delete_Harness',text='delete', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    },orderable = False)

    update = tables.LinkColumn('update_Harness',text='edit', args=[A('pk')], attrs={
    'a': {'class': 'btn', 'target': '_blank'}
    }, orderable = False)
    
    harness_name = tables.LinkColumn('harness_info', args=[A('pk')], attrs={
    'a': {'class': 'btn', 'target': '_blank'}
    }, orderable = True)

    class Meta:
        model = Harness
        exclude = ("harness_id", )


class SkillTable(ColumnShiftTableBootstrap3):
    delete = tables.LinkColumn('delete_Skill',text='delete', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    },orderable = False)

    update = tables.LinkColumn('update_Skill',text='edit', args=[A('pk')], attrs={
    'a': {'class': 'btn', 'target': '_blank'}
    }, orderable = False)

    class Meta:
        model = Skill
        exclude = ("skill_id", )


class LabTable(ColumnShiftTableBootstrap3):
    delete = tables.LinkColumn('delete_Lab',text='delete', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    },orderable = False)

    update = tables.LinkColumn('update_Lab',text='edit', args=[A('pk')], attrs={
    'a': {'class': 'btn', 'target': '_blank'}
    }, orderable = False)

    class Meta:
        model = Lab
        exclude = ("lab_id", )


class FluidTable(ColumnShiftTableBootstrap3):
    delete = tables.LinkColumn('delete_Fluid',text='delete', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    },orderable = False)

    update = tables.LinkColumn('update_Fluid',text='edit', args=[A('pk')], attrs={
    'a': {'class': 'btn', 'target': '_blank'}
    }, orderable = False)

    class Meta:
        model = Fluid
        exclude = ("fluid_id", )


class TechnicianTable(ColumnShiftTableBootstrap3):
    delete = tables.LinkColumn('delete_Technician',text='delete', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    },orderable = False)

    update = tables.LinkColumn('update_Technician',text='edit', args=[A('pk')], attrs={
    'a': {'class': 'btn', 'target': '_blank'}
    }, orderable = False)

    class Meta:
        model = Technician
        exclude = ("technician_id", )


class TestTypeTable(ColumnShiftTableBootstrap3):
    delete = tables.LinkColumn('delete_TestType',text='delete', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    },orderable = False)

    update = tables.LinkColumn('update_TestType',text='edit', args=[A('pk')], attrs={
    'a': {'class': 'btn', 'target': '_blank'}
    }, orderable = False)

    class Meta:
        model = TestType
        exclude = ("test_type_id", )


class ProgramTable(ColumnShiftTableBootstrap3):
    delete = tables.LinkColumn('delete_program',text='delete', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    },orderable = False)

    update = tables.LinkColumn('update_program',text='edit', args=[A('pk')], attrs={
    'a': {'class': 'btn', 'target': '_blank'}
    }, orderable = False)

    clone = tables.LinkColumn('clone2',text='clone', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    }, orderable = False)
    

    class Meta:
        model = Program
        exclude = ("program_id", )


class CageTable(ColumnShiftTableBootstrap3):
    delete = tables.LinkColumn('delete_cage',text='delete', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    },orderable = False)

    update = tables.LinkColumn('update_cage',text='edit', args=[A('pk')], attrs={
    'a': {'class': 'btn', 'target': '_blank'}
    }, orderable = False)


    class Meta:
        model = Cage
        exclude = ("cage_id", )


class DarTable(ColumnShiftTableBootstrap3):
    delete = tables.LinkColumn('delete_Dar',text='delete', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    },orderable = False)

    update = tables.LinkColumn('update_Dar',text='edit', args=[A('pk')], attrs={
    'a': {'class': 'btn', 'target': '_blank'}
    }, orderable = False)


    class Meta:
        model = DAR
        exclude = ("dar_id", )


class ChamberTable(ColumnShiftTableBootstrap3):
    delete = tables.LinkColumn('delete_Chamber',text='delete', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    },orderable = False)

    update = tables.LinkColumn('update_Chamber',text='edit', args=[A('pk')], attrs={
    'a': {'class': 'btn', 'target': '_blank'}
    }, orderable = False)


    class Meta:
        model = Chamber
        exclude = ("chamber_id", )

class ProductTable(ColumnShiftTableBootstrap3):
    delete = tables.LinkColumn('delete_product',text='delete', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    }, orderable = False)

    update = tables.LinkColumn('update_product',text='edit', args=[A('pk')], attrs={
    'a': {'class': 'btn', 'target': '_blank'}
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
    'a': {'class': 'btn', 'target': '_blank'}
    }, orderable = False)

    clone = tables.LinkColumn('clone',text='clone', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    }, orderable = False)

    log = tables.LinkColumn('find',text='log', args=[A('pk')], attrs={
    'a': {'class': 'btn', 'target': '_blank'}
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
    'a': {'class': 'btn', 'target': '_blank'}
    }, orderable = False)

    clone = tables.LinkColumn('clone3',text='clone', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    }, orderable = False)

    id = tables.LinkColumn('ChamberLog', args=[A('pk')], attrs={
    'a': {'class': 'btn', 'target': '_blank'}
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

class TestMapTable(ColumnShiftTableBootstrap3):

    class Meta:
        model = TestMap
        exclude = ("program_id", )
        
        
class DUTTable(ColumnShiftTableBootstrap3):
    delete = tables.LinkColumn('delete_dut',text='delete', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    }, orderable = False)

    update = tables.LinkColumn('update_dut',text='edit', args=[A('pk')], attrs={
    'a': {'class': 'btn', 'target': '_blank'}
    }, orderable = False)
    
    dut_name = tables.LinkColumn('dut_info', args=[A('pk')], attrs={
    'a': {'class': 'btn', 'target': '_blank'}
    }, orderable = True)

    class Meta:
        model = DUT
        exclude = ("dut_id", )
        
class SubcomponentTable(ColumnShiftTableBootstrap3):
    delete = tables.LinkColumn('delete_subcomponent',text='delete', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    }, orderable = False)

    update = tables.LinkColumn('update_subcomponent',text='edit', args=[A('pk')], attrs={
    'a': {'class': 'btn', 'target': '_blank'}
    }, orderable = False)

    class Meta:
        model = Subcomponent
        exclude = ("component_id","dut_id" )

class DAR_ChannelTable(ColumnShiftTableBootstrap3):
    delete = tables.LinkColumn('delete_DAR_Channel',text='delete', args=[A('pk')], attrs={
    'a': {'class': 'btn'}
    }, orderable = False)

    update = tables.LinkColumn('update_DAR_Channel',text='edit', args=[A('pk')], attrs={
    'a': {'class': 'btn', 'target': '_blank'}
    }, orderable = False)

    class Meta:
        model = DARChannel
        exclude = ("channel_id", )