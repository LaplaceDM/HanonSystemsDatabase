from django.db import models
from django.db.models import Model 
from django.utils import timezone
from dbview.models import DbView


# Create your models here.

class Program(models.Model):
    created = models.DateTimeField(default=timezone.now)
    program_name = models.CharField(max_length = 50, verbose_name = "Program",  null = True) 
    status = models.CharField(max_length = 20, verbose_name = "Status",  null = True)
    phase = models.CharField(max_length = 20, verbose_name = "Phase",  null = True)
    enterproj_id = models.IntegerField(null = True)
    wbs_number = models.CharField(max_length = 30, null = True)
    oem = models.CharField(max_length = 20, null = True)
    
    program_id = models.SmallAutoField(primary_key=True)

    def __str__(self):
        return self.program_name

class Lab(models.Model):
    lab_name = models.CharField(max_length = 20, null = True)
    city = models.CharField(max_length = 20, null = True)
    country = models.CharField(max_length = 15, null = True)
    supervisor = models.CharField(max_length = 25, null = True)
    
    lab_id = models.SmallAutoField(primary_key=True)
    def __str__(self):
        return self.lab_name

class Product(models.Model):
    created = models.DateTimeField(default=timezone.now)
    product_family = models.CharField(max_length = 10, null = True)
    platform = models.CharField(max_length = 15, null = True)
    communication_protocol = models.CharField(max_length = 15, null = True)
    voltage = models.CharField(max_length = 3, null = True)
    variant = models.CharField(max_length = 30, null = True)
    
    product_id = models.AutoField(primary_key=True)
    program_id = models.ForeignKey( "Program", on_delete = models.CASCADE, null = True, db_column="program_id")
    def __str__(self):
        return self.product_family

class TestMap(models.Model):
    test_map_name = models.CharField(max_length = 30, null = True)
    tr = models.CharField(max_length = 14, unique= True, null = True)
    test_map_id = models.AutoField(primary_key=True)

    program_id = models.ForeignKey( "Program", on_delete = models.CASCADE, null = True, db_column="program_id")
    def __str__(self):
        return self.tr + (" - ")  +str(self.test_map_name)

class Technician (models.Model):
    technician_name = models.CharField(max_length = 30)
    technician_id = models.SmallAutoField(primary_key=True)
    
    lab_id = models.ForeignKey( "Lab", on_delete = models.SET_NULL, null = True, db_column = "lab_id")
    def __str__(self):
        return self.technician_name

class Skill (models.Model):
    skill = models.CharField(max_length = 25, unique=True)
    skill_id = models.SmallAutoField(primary_key=True)

class Technician_Skill (models.Model):
    id = models.AutoField(primary_key=True)

    skill_id = models.ForeignKey("Skill", on_delete = models.CASCADE, db_column="skill_id")
    technician_id = models.ForeignKey("Technician", on_delete = models.CASCADE, db_column="technician_id")

class DUT(models.Model):
    dut_name = models.CharField(max_length = 12, unique = True)
    received_date = models.DateField(null = True)
    storage_date = models.DateField(null = True)
    storage_bin = models.CharField(max_length = 20, null = True)

    dut_id = models.BigAutoField(primary_key=True)
    product_id = models.ForeignKey("Product", on_delete = models.SET_NULL, null = True, db_column = "product_id")

class Test_DUT(models.Model):
    date = models.DateField(null = True)
    circuit_number = models.SmallIntegerField(null = True)
    id = models.BigAutoField(primary_key=True)

    test_id = models.ForeignKey("Test", on_delete = models.CASCADE, db_column = "test_id")
    dut_id = models.ForeignKey("DUT", on_delete = models.CASCADE, db_column = "dut_id")

class Test_Harness(models.Model):
    date = models.DateField(null = True)
    circuit_number = models.SmallIntegerField(null = True)
    id = models.BigAutoField(primary_key=True)

    test_id = models.ForeignKey("Test", on_delete = models.CASCADE, db_column = "test_id")
    harness_id = models.ForeignKey("Harness", on_delete = models.CASCADE, db_column = "harness_id")

class Fluid(models.Model):
    fluid_name = models.CharField(max_length = 30)
    manufacturer = models.CharField(max_length = 20, null = True)
    storage_location = models.CharField(max_length = 20, null = True)
    fluid_id = models.SmallAutoField(primary_key=True)

class Harness(models.Model):
    harness_id = models.BigAutoField(primary_key=True)
    harness_name = models.CharField(max_length = 50, unique= True)
    storage_location = models.CharField(max_length = 20, null = True)
    test_screening_resutl = models.CharField(max_length = 10, verbose_name = "Test Screening Result",  null = True)
    harness_connector_condition = models.CharField(max_length = 10, verbose_name = "Harness Connector Condition",  null = True)
    insulation_condition = models.CharField(max_length = 10, verbose_name = "Insulation Condition",  null = True)
    rtv_condition = models.CharField(max_length = 10, verbose_name = "RTV Condition",  null = True)
    dunk_testing = models.CharField(max_length = 10, verbose_name = "Dunk Testing",  null = True)
    average_resistance = models.FloatField(null = True)
    comments = models.CharField(max_length = 50)

class Test(models.Model):
    created = models.DateTimeField(default=timezone.now)
    product_id = models.ForeignKey("Product", on_delete = models.SET_NULL, null = True, db_column = "product_id")
    program_id = models.ForeignKey( "Program", on_delete = models.CASCADE, null = True, db_column="program_id")
    test_map_id = models.ForeignKey("TestMap", on_delete = models.CASCADE, db_column = "test_map_id", verbose_name = "Leg")
    priority = models.SmallIntegerField(null = True)
    scheduling = models.CharField(max_length = 15, null =True)
    status = models.CharField(max_length = 15, null =True)
    test_type_id = models.ForeignKey("TestType", on_delete = models.CASCADE, db_column = "test_type_id", verbose_name = "Test")
    test_id = models.AutoField(primary_key=True)
    technician_id = models.ForeignKey("Technician", on_delete = models.CASCADE, db_column = "technician_id", verbose_name = "technician")
    chamber_id = models.ForeignKey("Chamber", on_delete = models.CASCADE, db_column = "chamber_id", verbose_name = "chamber")
    dar_id = models.ForeignKey("DAR", on_delete = models.CASCADE, db_column = "dar_id", verbose_name = "DAR")
    cage_id = models.ForeignKey("Cage", on_delete = models.CASCADE, db_column = "cage_id", verbose_name = "cage")
    lab_id = models.ForeignKey("Lab", on_delete = models.CASCADE, db_column = "lab_id", verbose_name = "Lab")
    total_hours = models.SmallIntegerField(null = True)

    targeted_start = models.DateField(null =True)
    targeted_end = models.DateField(null =True)
    supervisor_comments = models.CharField(max_length = 4000, null =True)
    hours_planned = models.SmallIntegerField(null =True)
    setup_date = models.DateField(null =True)
    
    status_log = models.CharField(max_length = 4000, null = True)
    def __str__(self):
        return f"{self.test_type_id} {self.chamber_id}"

class ChamberLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    timestamp = models.DateTimeField()
    circuit_number = models.SmallIntegerField()
    total_hours = models.SmallIntegerField()
    status = models.CharField(max_length = 20, verbose_name = "Status",  null = True)
    fluid_temp = models.FloatField(null = True)
    ambient_temp = models.FloatField(null = True)
    system_pressure = models.FloatField(null = True)
    lin_speed = models.FloatField(null = True)
    voltage = models.FloatField(null = True)
    current = models.FloatField(null = True)
    head = models.FloatField(null = True)
    comments = models.CharField(max_length = 300)

    log_id = models.ForeignKey("ChamberLogInfo", on_delete = models.CASCADE, db_column = "log_id")

class ChamberLogInfo(DbView):
    created = models.DateTimeField(default=timezone.now)
    id = models.AutoField(primary_key=True)
    pretest_inspection_and_photo = models.CharField(max_length = 10, verbose_name = "Pretest Inspection and Photo",  null = True)
    setup_photo = models.FloatField(null = True)
    humidity = models.FloatField(null = True)
    system_pressure = models.FloatField(null = True)
    voltage = models.FloatField(null = True)
    system_restriction_target = models.CharField(max_length = 50,null = True)
    system_restriction_record = models.CharField(max_length = 10, verbose_name = "System Restriction Record",  null = True)
    trial_run_record_and_process = models.CharField(max_length = 10, verbose_name = "Trial Run Record And Process",  null = True)
    special_requirements = models.CharField(max_length = 300,null = True)

    test_id = models.ForeignKey("Test", on_delete = models.CASCADE, db_column = "test_id")
    chamber_id = models.ForeignKey("Chamber", on_delete = models.CASCADE, db_column = "chamber_id")
    program_id = models.ForeignKey("Program", on_delete = models.CASCADE, db_column = "program_id")
    technician_id = models.ForeignKey("Technician", on_delete = models.CASCADE, db_column = "technician_id")

class Cage (models.Model):
    cage_id = models.SmallAutoField(primary_key=True)
    cage_name = models.CharField(max_length = 20, unique = True)
    number_of_duts = models.SmallIntegerField(null=True)
    def __str__(self):
        return self.cage_name

class TestType (models.Model):
    test_type_id = models.SmallAutoField(primary_key=True)
    test_name = models.CharField(max_length = 20, unique = True)
    def __str__(self):
        return self.test_name

class DAR (models.Model):
    dar_id = models.SmallAutoField(primary_key=True)
    dar_name = models.CharField(max_length = 20, unique = True)
    ac_input_voltage = models.SmallIntegerField(null = True)
    ac_input_phase = models.CharField(max_length = 20, null = True)
    operation_team = models.CharField(max_length = 20, null = True)
    working_condition = models.CharField(max_length = 50, verbose_name = "Working Condition",  null = True)

    lab_id = models.ForeignKey("Lab", on_delete = models.SET_NULL, null=True, db_column = "lab_id")
    def __str__(self):
        return self.dar_name

class Chamber(models.Model):
    chamber_id = models.SmallAutoField(primary_key=True)
    chamber_name = models.CharField(max_length = 20, unique= True)
    cooling_type = models.CharField(max_length = 20, null=True)
    power = models.SmallIntegerField(null=True)
    humidity = models.CharField(max_length = 10, verbose_name = "Humidity",  null = True)
    operation_team = models.CharField(max_length = 20, null=True)
    working_condition = models.CharField(max_length = 50, verbose_name = "Working Condition",  null = True)
    rate = models.FloatField(null=True)
    currency = models.CharField(max_length = 20, null=True)
    heating_power = models.SmallIntegerField()
    cooling_power = models.SmallIntegerField()
    heating_gradient = models.FloatField()

    lab_id = models.ForeignKey("Lab", on_delete = models.SET_NULL, null=True, db_column = "lab_id")
    def __str__(self):
        return self.chamber_name

class Laptop(models.Model):
    laptop_id = models.SmallAutoField(primary_key=True)
    laptop_name = models.CharField(max_length =20, unique= True)
    brand = models.CharField(max_length = 20, null=True)
    mac_address = models.CharField(max_length = 30 , null=True)
    system_type = models.CharField(max_length = 20, null=True)
    ram_slot1= models.SmallIntegerField(null=True)
    ram_slot2 =models.SmallIntegerField(null=True)
    total_ram = models.SmallIntegerField(null=True)
    ram_limit = models.SmallIntegerField(null=True)
    ram_type = models.CharField(max_length= 20, null=True)
    ram_upgrade_date = models.DateField(null=True)
    mfg_year = models.SmallIntegerField(null=True)
    model = models.CharField(max_length = 30, null=True)
    model_number = models.CharField(max_length = 30, null=True)
    serial_number = models.CharField(max_length =30, null=True)
    operating_system = models.CharField(max_length = 20, null =True)
    keyboard_cover = models.CharField(max_length = 10, verbose_name = "Keyboard Cover",  null = True)
    comments = models.CharField(max_length= 300, null =True)

class Test_Chamber (models.Model):
    id = models.SmallAutoField(primary_key=True)
    test_type_id = models.SmallIntegerField(null =True)
    test_type_id = models.ForeignKey("TestType", on_delete = models.CASCADE, null =True, db_column = "test_type_id")
    
    chamber_id = models.ForeignKey("Chamber", on_delete = models.CASCADE, null =True, db_column = "chamber_id")

class DAR_Laptop(models.Model):
    id = models.SmallAutoField(primary_key=True)

    dar_id = models.ForeignKey("DAR", on_delete = models.CASCADE, null =True, db_column = "dar_id")
    laptop_id = models.ForeignKey("Laptop", on_delete = models.CASCADE, null =True, db_column = "laptop_id")

class DARChannel(models.Model):
    channel_id = models.SmallIntegerField(primary_key=True)
    channel_number = models.SmallIntegerField(null =True)
    power_supply_type = models.CharField(max_length = 20, null =True)
    power_supply_voltage = models.SmallIntegerField(null =True)
    max_current = models.SmallIntegerField(null =True)
    lin = models.CharField(max_length = 50, verbose_name = "LIN",  null = True)
    pwn = models.CharField(max_length = 50, verbose_name = "PWN",  null = True)
    can = models.CharField(max_length = 50, verbose_name = "CAN",  null = True)

    dar_id = models.ForeignKey("DAR", on_delete = models.CASCADE, null =True, db_column = "dar_id")
    def __str__(self):
        return str(self.channel_number)

class Program_Fluid(models.Model):
    id = models.AutoField(primary_key=True)

    program_id = models.ForeignKey("Program", on_delete = models.CASCADE, null =True, db_column = "program_id")
    fluid_id = models.ForeignKey("Fluid", on_delete = models.CASCADE, null =True, db_column = "fluid_id")

class Program_DAR(models.Model):
    id = models.AutoField(primary_key=True)

    program_id = models.ForeignKey("Program", on_delete = models.CASCADE, null =True, db_column = "program_id")
    dar_id = models.ForeignKey("DAR", on_delete = models.CASCADE, null =True, db_column = "dar_id")

class Program_Cage(models.Model):
    id = models.AutoField(primary_key=True)

    program_id = models.ForeignKey("Program", on_delete = models.CASCADE, null =True, db_column = "program_id")
    cage_id = models.ForeignKey("Cage", on_delete = models.CASCADE, null =True, db_column = "cage_id")