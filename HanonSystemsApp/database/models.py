from django.db import models
from django.db.models import Model 
from django.utils import timezone



# Create your models here.

class Program(models.Model):
    program_name = models.CharField(max_length = 50, verbose_name = "Program",  null = True) 
    status = models.CharField(max_length = 20, verbose_name = "Status",  null = True)
    phase = models.CharField(max_length = 10, verbose_name = "Phase",  null = True)
    enterproj_id = models.CharField(max_length = 10, verbose_name = "EnterProj ID",  null = True)
    wbs_number = models.CharField(max_length = 30, null = True, verbose_name = "WBS")
    oem = models.CharField(max_length = 20, null = True, verbose_name = "OEM")
    
    program_id = models.SmallAutoField(primary_key=True)

    def __str__(self):
        return self.program_name

class Lab(models.Model):
    lab_name = models.CharField(max_length = 20, null = True)
    city = models.CharField(max_length = 20, null = True)
    country = models.CharField(max_length = 15, null = True)
    supervisor = models.CharField(max_length = 25, null = True)
    
    lab_id = models.SmallAutoField(primary_key=True, verbose_name = "Lab")
    def __str__(self):
        return self.lab_name

class Product(models.Model):
    product_family = models.CharField(max_length = 10, null = True)
    platform = models.CharField(max_length = 15, null = True)
    communication_protocol = models.CharField(max_length = 15, null = True)
    voltage = models.CharField(max_length = 3, null = True)
    variant = models.CharField(max_length = 30, null = True)
    
    product_id = models.AutoField(primary_key=True, verbose_name = "Product")
    program_id = models.ForeignKey( "Program", on_delete = models.CASCADE, null = True, db_column="program_id", verbose_name = "Program")
    def __str__(self):
        return self.product_family+ (" - ")  +str(self.program_id.program_name)

class TestMap(models.Model):
    test_map_name = models.CharField(max_length = 30, null = True, verbose_name = "Test Map name")
    tr = models.CharField(max_length = 14, unique= True, null = True, verbose_name = "TR")
    test_map_id = models.AutoField(primary_key=True)

    program_id = models.ForeignKey( "Program", on_delete = models.CASCADE, null = True, db_column="program_id", verbose_name = "Program")
    def __str__(self):
        return self.tr + (" - ")  +str(self.test_map_name)

class Technician (models.Model):
    technician_name = models.CharField(max_length = 30)
    technician_id = models.SmallAutoField(primary_key=True)
    
    lab_id = models.ForeignKey( "Lab", on_delete = models.SET_NULL, null = True, db_column = "lab_id", verbose_name = "Lab")
    def __str__(self):
        return self.technician_name

class Skill (models.Model):
    skill = models.CharField(max_length = 25, unique=True)
    skill_id = models.SmallAutoField(primary_key=True)
    def __str__(self):
        return self.skill

class Technician_Skill (models.Model):
    id = models.AutoField(primary_key=True)

    skill_id = models.ForeignKey("Skill", on_delete = models.CASCADE, db_column="skill_id", verbose_name = "Skill")
    technician_id = models.ForeignKey("Technician", on_delete = models.CASCADE, db_column="technician_id", verbose_name = "Technician name")

class DUT(models.Model):
    dut_name = models.CharField(max_length = 40, unique = True, verbose_name = "DUT name")
    received_date = models.DateField(null = True)
    storage_date = models.DateField(null = True)
    storage_bin = models.CharField(max_length = 20, null = True)
    pedigree = models.CharField(max_length = 30, null = True)

    dut_id = models.BigAutoField(primary_key=True, verbose_name = "DUT name")
    product_id = models.ForeignKey("Product", on_delete = models.SET_NULL, null = True, db_column = "product_id", verbose_name = "Product - Program")
    
    def __str__(self):
        return self.dut_name + " - " + self.product_id.program_id.program_name

class Test_DUT(models.Model):
    circuit_number = models.SmallIntegerField(null = True)
    id = models.BigAutoField(primary_key=True)
    date_inserted = models.DateTimeField()
    date_removed = models.DateTimeField(null = True)
    test_id = models.ForeignKey("Test", on_delete = models.CASCADE, db_column = "test_id", verbose_name = "Test")
    dut_id = models.ForeignKey("DUT", on_delete = models.CASCADE, db_column = "dut_id", verbose_name = "DUT name")
    
class Subcomponent(models.Model):
    subcomponent_name = models.CharField(max_length = 100)
    subcomponent_id = models.BigAutoField(primary_key=True, verbose_name = "Subcomponent")
    software = models.CharField(max_length = 100, null=True)
    hardware = models.CharField(max_length = 100, null=True)
    dut_id = models.ForeignKey("DUT", on_delete = models.CASCADE, null = True, db_column = "dut_id", verbose_name = "DUT name")

class Test_Harness(models.Model):
    circuit_number = models.SmallIntegerField(null = True)
    id = models.BigAutoField(primary_key=True)
    date_inserted = models.DateTimeField()
    date_removed = models.DateTimeField(null = True)
    test_id = models.ForeignKey("Test", on_delete = models.CASCADE, db_column = "test_id", verbose_name = "Test")
    harness_id = models.ForeignKey("Harness", on_delete = models.CASCADE, db_column = "harness_id", verbose_name = "Harness name")

class Fluid(models.Model):
    fluid_name = models.CharField(max_length = 30)
    manufacturer = models.CharField(max_length = 20, null = True)
    storage_location = models.CharField(max_length = 20, null = True)
    fluid_id = models.SmallAutoField(primary_key=True, verbose_name = "Fluid name")
    def __str__(self):
        return self.manufacturer +" - "+ self.fluid_name

class Harness(models.Model):
    harness_id = models.BigAutoField(primary_key=True)
    harness_name = models.CharField(max_length = 40)
    storage_location = models.CharField(max_length = 40, null = True)
    test_screening_result = models.CharField(max_length = 4, verbose_name = "Test Screening Result",  null = True)
    harness_connector_condition = models.CharField(max_length = 4, verbose_name = "Harness Connector Condition",  null = True)
    insulation_condition = models.CharField(max_length = 4, verbose_name = "Insulation Condition",  null = True)
    rtv_condition = models.CharField(max_length = 4, verbose_name = "RTV Condition",  null = True)
    dunk_testing = models.CharField(max_length = 4, verbose_name = "Dunk Testing",  null = True)
    average_resistance = models.FloatField(null = True)
    comments = models.CharField(max_length = 200, null= True)
    def __str__(self):
        return self.harness_name
    
class Test(models.Model):
    created = models.DateTimeField(default=timezone.now)
    product_id = models.ForeignKey("Product", on_delete = models.SET_NULL, null = True, db_column = "product_id", verbose_name = "Product")
    program_id = models.ForeignKey( "Program", on_delete = models.CASCADE, null = True, db_column="program_id", verbose_name = "Program")
    test_map_id = models.ForeignKey("TestMap", on_delete = models.CASCADE, db_column = "test_map_id", verbose_name = "Leg")
    priority = models.SmallIntegerField(null = True)
    scheduling = models.CharField(max_length = 15, null =True)
    status = models.CharField(max_length = 15, null =True)
    test_type_id = models.ForeignKey("TestType", on_delete = models.CASCADE, db_column = "test_type_id", verbose_name = "Test Type")
    test_description = models.CharField(max_length = 100, null =True)
    test_id = models.AutoField(primary_key=True)
    technician_id = models.ForeignKey("Technician", on_delete = models.CASCADE, db_column = "technician_id", verbose_name = "Technician")
    chamber_id = models.ForeignKey("Chamber", on_delete = models.CASCADE, db_column = "chamber_id", verbose_name = "Chamber")
    dar_id = models.ForeignKey("DAR", on_delete = models.CASCADE, db_column = "dar_id", verbose_name = "DAR")
    cage_id = models.ForeignKey("Cage", on_delete = models.CASCADE, db_column = "cage_id", verbose_name = "Cage")
    lab_id = models.ForeignKey("Lab", on_delete = models.CASCADE, db_column = "lab_id", verbose_name = "Lab")

    targeted_start = models.DateField(null =True)
    targeted_end = models.DateField(null =True)
    supervisor_comments = models.CharField(max_length = 4000, null =True)
    hours_planned = models.SmallIntegerField(null =True)
    total_hours = models.SmallIntegerField(null = True)

    def __str__(self):
        return f"{self.test_map_id.tr} - {self.test_type_id}: {self.test_description}"

class ChamberLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    timestamp = models.DateTimeField()
    circuit_number = models.SmallIntegerField()
    total_hours = models.SmallIntegerField()
    status = models.CharField(max_length = 20, verbose_name = "Status",  null = True)
    chamber_id = models.ForeignKey("Chamber", on_delete = models.CASCADE, db_column = "chamber_id", verbose_name = "Chamber")
    comments = models.CharField(max_length = 300, null = True)
    technician = models.CharField(max_length = 100, null = True)
    shaker_direction = models.CharField(max_length = 100, null = True)
    dar_id = models.ForeignKey("DAR", on_delete = models.CASCADE, db_column = "dar_id", null = True, verbose_name = "DAR")
    cage_id = models.ForeignKey("Cage", on_delete = models.CASCADE, db_column = "cage_id", null = True, verbose_name = "Cage")
    
    log_id = models.ForeignKey("ChamberLogInfo", on_delete = models.CASCADE, db_column = "log_id", verbose_name = "Log")
    
    

class ChamberLogInfo(models.Model):
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
    coolant = models.CharField(max_length = 100, null = True)
    temperature = models.FloatField(null = True)
    test_profile = models.CharField(max_length = 300, null = True)
    shaker_profile = models.CharField(max_length = 300, null = True)
    chamber_profile = models.CharField(max_length = 300, null = True)
    pump_profile = models.CharField(max_length = 300, null = True)
    chamber_id = models.ForeignKey("Chamber", on_delete = models.SET_NULL, null=True, db_column = "chamber_id", verbose_name = "Chamber")
    program_id = models.ForeignKey("Program", on_delete = models.SET_NULL, null=True, db_column = "program_id", verbose_name = "Program")
    technician_id= models.ForeignKey("Technician", on_delete = models.SET_NULL, null=True, db_column = "technician_id", verbose_name = "Technician")
    comments = models.CharField(max_length = 4000, null = True)

    test_id = models.ForeignKey("Test", on_delete = models.CASCADE, db_column = "test_id", verbose_name = "Test")
    def __str__(self):
        return f"{self.test_id}"

class Cage (models.Model):
    cage_id = models.SmallAutoField(primary_key=True)
    cage_name = models.CharField(max_length = 20)
    number_of_duts = models.SmallIntegerField(null=True)
    category = models.CharField(max_length=20, null=True)
    product = models.CharField(max_length=10, null=True)
    def __str__(self):
        return self.cage_name

class TestType (models.Model):
    test_type_id = models.SmallAutoField(primary_key=True)
    test_name = models.CharField(max_length = 50, db_column = "test_type", verbose_name = "test_type")
    def __str__(self):
        return self.test_name

class DAR (models.Model):
    dar_id = models.SmallAutoField(primary_key=True)
    dar_name = models.CharField(max_length = 40, unique = True)
    ac_input_voltage = models.CharField(max_length = 20,null = True)
    ac_input_phase = models.CharField(max_length = 30, null = True)
    operation_team = models.CharField(max_length = 20, null = True)
    working_condition = models.CharField(max_length = 50, verbose_name = "Working Condition",  null = True)

    lab_id = models.ForeignKey("Lab", on_delete = models.SET_NULL, null=True, db_column = "lab_id", verbose_name = "Lab")
    def __str__(self):
        return self.dar_name

class Chamber(models.Model):
    chamber_id = models.SmallAutoField(primary_key=True)
    chamber_name = models.CharField(max_length = 20, unique= True)
    cooling_type = models.CharField(max_length = 20, null=True)
    power = models.CharField(max_length=20,null=True)
    humidity = models.CharField(max_length = 3, verbose_name = "Humidity",  null = True)
    operation_team = models.CharField(max_length = 20, null=True)
    working_condition = models.CharField(max_length = 50, verbose_name = "Working Condition",  null = True)
    rate = models.FloatField(null=True)
    currency = models.CharField(max_length = 20, null=True)
    heating_power = models.SmallIntegerField(null = True)
    cooling_power = models.SmallIntegerField(null = True)
    heating_gradient = models.FloatField(null = True)
    max_daily_hours = models.SmallIntegerField(null = True)
    billing_category = models.CharField(max_length = 30, null = True)

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
    processor_type = models.SmallIntegerField(null=True, verbose_name="Processor Type (32 or 64)")
    ram_type = models.CharField(max_length= 20, null=True)
    ram_upgrade_date = models.DateField(null=True)
    mfg_year = models.SmallIntegerField(null=True)
    model = models.CharField(max_length = 30, null=True)
    model_number = models.CharField(max_length = 30, null=True)
    serial_number = models.CharField(max_length =30, null=True)
    operating_system = models.CharField(max_length = 20, null =True)
    keyboard_cover = models.CharField(max_length = 3, verbose_name = "Keyboard Cover",  null = True)
    teamviewer_id = models.CharField(max_length = 20,  null = True)
    status = models.CharField(max_length = 25,  null = True)
    comments = models.CharField(max_length= 300, null =True)
    dar = models.ForeignKey("DAR", on_delete = models.SET_NULL, null =True, verbose_name="DAR")

class Test_Chamber (models.Model):
    id = models.SmallAutoField(primary_key=True)
    test_type_id = models.ForeignKey("TestType", on_delete = models.CASCADE, null =True, db_column = "test_type_id", verbose_name = "Test")
    
    chamber_id = models.ForeignKey("Chamber", on_delete = models.CASCADE, null =True, db_column = "chamber_id", verbose_name = "Chamber")

class DARChannel(models.Model):
    channel_id = models.AutoField(primary_key=True)
    channel_number = models.SmallIntegerField(null =True)
    number_of_duts = models.SmallIntegerField(null =True)
    power_supply_type = models.CharField(max_length = 20, null =True)
    power_supply_48V = models.SmallIntegerField(null =True)
    power_supply_12V = models.SmallIntegerField(null =True)
    max_current_48V = models.CharField(max_length = 10, null =True)
    max_current_12V = models.CharField(max_length = 10, null =True)
    power_supply_model = models.CharField(max_length = 50,  null = True)
    eWP_Primary = models.CharField(max_length = 3,null =True)
    eWP_Med_Aux = models.CharField(max_length = 3,null =True)
    eTMOP = models.CharField(max_length = 3,null =True)
    eCF = models.CharField(max_length = 3,null =True)
    lin = models.CharField(max_length = 50, verbose_name = "LIN",  null = True)
    pwn = models.CharField(max_length = 50, verbose_name = "PWN",  null = True)
    can = models.CharField(max_length = 50, verbose_name = "CAN",  null = True)
    pressure_transducer_inlet = models.CharField(max_length = 50, null =True)
    pressure_transducer_outlet = models.CharField(max_length = 50, null =True)
    
    
    dar_id = models.ForeignKey("DAR", on_delete = models.CASCADE, null =True, db_column = "dar_id", verbose_name="DAR")
    def __str__(self):
        return str(self.dar_id.dar_name) + "-" + str(self.channel_number)

class Program_Fluid(models.Model):
    id = models.AutoField(primary_key=True)

    program_id = models.ForeignKey("Program", on_delete = models.CASCADE, null =True, db_column = "program_id", verbose_name = "Program")
    fluid_id = models.ForeignKey("Fluid", on_delete = models.CASCADE, null =True, db_column = "fluid_id", verbose_name = "Fluid")

class Program_DAR(models.Model):
    id = models.AutoField(primary_key=True)

    program_id = models.ForeignKey("Program", on_delete = models.CASCADE, null =True, db_column = "program_id", verbose_name = "Program")
    dar_id = models.ForeignKey("DAR", on_delete = models.CASCADE, null =True, db_column = "dar_id", verbose_name = "DAR")

class Program_Cage(models.Model):
    id = models.AutoField(primary_key=True)

    program_id = models.ForeignKey("Program", on_delete = models.CASCADE, null =True, db_column = "program_id", verbose_name = "Program")
    cage_id = models.ForeignKey("Cage", on_delete = models.CASCADE, null =True, db_column = "cage_id", verbose_name = "Cage")