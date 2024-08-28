# Generated by Django 4.2.4 on 2024-08-27 13:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cage',
            fields=[
                ('cage_id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('cage_name', models.CharField(max_length=20)),
                ('number_of_duts', models.SmallIntegerField(null=True)),
                ('category', models.CharField(max_length=20, null=True)),
                ('product', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Chamber',
            fields=[
                ('chamber_id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('chamber_name', models.CharField(max_length=20, unique=True)),
                ('cooling_type', models.CharField(max_length=20, null=True)),
                ('power', models.CharField(max_length=20, null=True)),
                ('humidity', models.CharField(max_length=3, null=True, verbose_name='Humidity')),
                ('operation_team', models.CharField(max_length=20, null=True)),
                ('working_condition', models.CharField(max_length=50, null=True, verbose_name='Working Condition')),
                ('rate', models.FloatField(null=True)),
                ('currency', models.CharField(max_length=20, null=True)),
                ('heating_power', models.SmallIntegerField(null=True)),
                ('cooling_power', models.SmallIntegerField(null=True)),
                ('heating_gradient', models.FloatField(null=True)),
                ('max_daily_hours', models.SmallIntegerField(null=True)),
                ('billing_category', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DAR',
            fields=[
                ('dar_id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('dar_name', models.CharField(max_length=40, unique=True)),
                ('ac_input_voltage', models.CharField(max_length=20, null=True)),
                ('ac_input_phase', models.CharField(max_length=30, null=True)),
                ('operation_team', models.CharField(max_length=20, null=True)),
                ('working_condition', models.CharField(max_length=50, null=True, verbose_name='Working Condition')),
            ],
        ),
        migrations.CreateModel(
            name='DUT',
            fields=[
                ('dut_name', models.CharField(max_length=40, unique=True, verbose_name='DUT name')),
                ('received_date', models.DateField(null=True)),
                ('storage_date', models.DateField(null=True)),
                ('storage_bin', models.CharField(max_length=20, null=True)),
                ('pedigree', models.CharField(max_length=30, null=True)),
                ('dut_id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='DUT name')),
            ],
        ),
        migrations.CreateModel(
            name='Fixtures',
            fields=[
                ('fixture_name', models.CharField(max_length=50, null=True, verbose_name='Fixture Name')),
                ('product_id', models.CharField(max_length=10, null=True, verbose_name='Product ID')),
                ('number_of_DUTs', models.CharField(max_length=30, null=True, verbose_name='Number of DUTs')),
                ('comments', models.CharField(max_length=1000, null=True, verbose_name='Comments')),
                ('Fixtures_id', models.SmallAutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Fluid',
            fields=[
                ('fluid_name', models.CharField(max_length=30)),
                ('manufacturer', models.CharField(max_length=20, null=True)),
                ('storage_location', models.CharField(max_length=20, null=True)),
                ('fluid_id', models.SmallAutoField(primary_key=True, serialize=False, verbose_name='Fluid name')),
            ],
        ),
        migrations.CreateModel(
            name='Harness',
            fields=[
                ('harness_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('harness_name', models.CharField(max_length=40)),
                ('storage_location', models.CharField(max_length=40, null=True)),
                ('test_screening_result', models.CharField(max_length=4, null=True, verbose_name='Test Screening Result')),
                ('harness_connector_condition', models.CharField(max_length=4, null=True, verbose_name='Harness Connector Condition')),
                ('insulation_condition', models.CharField(max_length=4, null=True, verbose_name='Insulation Condition')),
                ('rtv_condition', models.CharField(max_length=4, null=True, verbose_name='RTV Condition')),
                ('dunk_testing', models.CharField(max_length=4, null=True, verbose_name='Dunk Testing')),
                ('average_resistance', models.FloatField(null=True)),
                ('comments', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('lab_name', models.CharField(max_length=20, null=True)),
                ('city', models.CharField(max_length=20, null=True)),
                ('country', models.CharField(max_length=15, null=True)),
                ('supervisor', models.CharField(max_length=25, null=True)),
                ('lab_id', models.SmallAutoField(primary_key=True, serialize=False, verbose_name='Lab')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_family', models.CharField(max_length=10, null=True)),
                ('platform', models.CharField(max_length=15, null=True)),
                ('communication_protocol', models.CharField(max_length=15, null=True)),
                ('voltage', models.CharField(max_length=3, null=True)),
                ('variant', models.CharField(max_length=30, null=True)),
                ('product_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Product')),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('program_name', models.CharField(max_length=50, null=True, verbose_name='Program')),
                ('status', models.CharField(max_length=20, null=True, verbose_name='Status')),
                ('phase', models.CharField(max_length=10, null=True, verbose_name='Phase')),
                ('enterproj_id', models.CharField(max_length=10, null=True, verbose_name='EnterProj ID')),
                ('wbs_number', models.CharField(max_length=30, null=True, verbose_name='WBS')),
                ('oem', models.CharField(max_length=20, null=True, verbose_name='OEM')),
                ('program_id', models.SmallAutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('skill', models.CharField(max_length=25, unique=True)),
                ('skill_id', models.SmallAutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Technician',
            fields=[
                ('technician_name', models.CharField(max_length=30)),
                ('technician_id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('lab_id', models.ForeignKey(db_column='lab_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.lab', verbose_name='Lab')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('priority', models.SmallIntegerField(null=True)),
                ('scheduling', models.TextField(max_length=300, null=True)),
                ('status', models.TextField(max_length=300, null=True)),
                ('test_description', models.TextField(max_length=150, null=True)),
                ('test_id', models.AutoField(primary_key=True, serialize=False)),
                ('targeted_start', models.DateField(null=True)),
                ('targeted_end', models.DateField(null=True)),
                ('supervisor_comments', models.TextField(max_length=18000, null=True)),
                ('hours_planned', models.SmallIntegerField(null=True)),
                ('total_hours', models.SmallIntegerField(null=True)),
                ('cage_id', models.ForeignKey(db_column='cage_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.cage', verbose_name='Cage')),
                ('chamber_id', models.ForeignKey(db_column='chamber_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.chamber', verbose_name='Chamber')),
                ('dar_id', models.ForeignKey(db_column='dar_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.dar', verbose_name='DAR')),
                ('lab_id', models.ForeignKey(db_column='lab_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.lab', verbose_name='Lab')),
                ('product_id', models.ForeignKey(db_column='product_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.product', verbose_name='Product')),
                ('program_id', models.ForeignKey(db_column='program_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.program', verbose_name='Program')),
                ('technician_id', models.ForeignKey(db_column='technician_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.technician', verbose_name='Technician')),
            ],
        ),
        migrations.CreateModel(
            name='TestType',
            fields=[
                ('test_type_id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('test_name', models.CharField(db_column='test_type', max_length=50, verbose_name='test_type')),
            ],
        ),
        migrations.CreateModel(
            name='TestMap',
            fields=[
                ('test_map_name', models.CharField(max_length=100, null=True, verbose_name='Test Map Name')),
                ('tr', models.CharField(max_length=14, null=True, verbose_name='TR')),
                ('test_map_id', models.AutoField(primary_key=True, serialize=False)),
                ('program_id', models.ForeignKey(db_column='program_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.program', verbose_name='Program')),
            ],
        ),
        migrations.CreateModel(
            name='Test_Harness',
            fields=[
                ('circuit_number', models.SmallIntegerField(null=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('date_inserted', models.DateTimeField()),
                ('date_removed', models.DateTimeField(null=True)),
                ('harness_id', models.ForeignKey(db_column='harness_id', on_delete=django.db.models.deletion.CASCADE, to='database.harness', verbose_name='Harness name')),
                ('test_id', models.ForeignKey(db_column='test_id', on_delete=django.db.models.deletion.CASCADE, to='database.test', verbose_name='Test')),
            ],
        ),
        migrations.CreateModel(
            name='Test_DUT',
            fields=[
                ('circuit_number', models.SmallIntegerField(null=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('date_inserted', models.DateTimeField()),
                ('date_removed', models.DateTimeField(null=True)),
                ('dut_id', models.ForeignKey(db_column='dut_id', on_delete=django.db.models.deletion.CASCADE, to='database.dut', verbose_name='DUT name')),
                ('test_id', models.ForeignKey(db_column='test_id', on_delete=django.db.models.deletion.CASCADE, to='database.test', verbose_name='Test')),
            ],
        ),
        migrations.CreateModel(
            name='Test_Chamber',
            fields=[
                ('id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('chamber_id', models.ForeignKey(db_column='chamber_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.chamber', verbose_name='Chamber')),
                ('test_type_id', models.ForeignKey(db_column='test_type_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.testtype', verbose_name='Test')),
            ],
        ),
        migrations.AddField(
            model_name='test',
            name='test_map_id',
            field=models.ForeignKey(db_column='test_map_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.testmap', verbose_name='Test Map'),
        ),
        migrations.AddField(
            model_name='test',
            name='test_type_id',
            field=models.ForeignKey(db_column='test_type_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.testtype', verbose_name='Test Type'),
        ),
        migrations.CreateModel(
            name='Technician_Skill',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('skill_id', models.ForeignKey(db_column='skill_id', on_delete=django.db.models.deletion.CASCADE, to='database.skill', verbose_name='Skill')),
                ('technician_id', models.ForeignKey(db_column='technician_id', on_delete=django.db.models.deletion.CASCADE, to='database.technician', verbose_name='Technician name')),
            ],
        ),
        migrations.CreateModel(
            name='Subcomponent',
            fields=[
                ('subcomponent_name', models.CharField(max_length=100)),
                ('subcomponent_id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Subcomponent')),
                ('software', models.CharField(max_length=100, null=True)),
                ('hardware', models.CharField(max_length=100, null=True)),
                ('dut_id', models.ForeignKey(db_column='dut_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.dut', verbose_name='DUT name')),
            ],
        ),
        migrations.CreateModel(
            name='Program_Fluid',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fluid_id', models.ForeignKey(db_column='fluid_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.fluid', verbose_name='Fluid')),
                ('program_id', models.ForeignKey(db_column='program_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.program', verbose_name='Program')),
            ],
        ),
        migrations.CreateModel(
            name='Program_DAR',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dar_id', models.ForeignKey(db_column='dar_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.dar', verbose_name='DAR')),
                ('program_id', models.ForeignKey(db_column='program_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.program', verbose_name='Program')),
            ],
        ),
        migrations.CreateModel(
            name='Program_Cage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cage_id', models.ForeignKey(db_column='cage_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.cage', verbose_name='Cage')),
                ('program_id', models.ForeignKey(db_column='program_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.program', verbose_name='Program')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='program_id',
            field=models.ForeignKey(db_column='program_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.program', verbose_name='Program'),
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('laptop_id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('laptop_name', models.CharField(max_length=20, unique=True)),
                ('brand', models.CharField(max_length=20, null=True)),
                ('mac_address', models.CharField(max_length=30, null=True)),
                ('system_type', models.CharField(max_length=20, null=True)),
                ('ram_slot1', models.SmallIntegerField(null=True)),
                ('ram_slot2', models.SmallIntegerField(null=True)),
                ('total_ram', models.SmallIntegerField(null=True)),
                ('processor_type', models.SmallIntegerField(null=True, verbose_name='Processor Type (32 or 64)')),
                ('ram_type', models.CharField(max_length=20, null=True)),
                ('ram_upgrade_date', models.DateField(null=True)),
                ('mfg_year', models.SmallIntegerField(null=True)),
                ('model', models.CharField(max_length=30, null=True)),
                ('model_number', models.CharField(max_length=30, null=True)),
                ('serial_number', models.CharField(max_length=30, null=True)),
                ('operating_system', models.CharField(max_length=20, null=True)),
                ('keyboard_cover', models.CharField(max_length=3, null=True, verbose_name='Keyboard Cover')),
                ('teamviewer_id', models.CharField(max_length=20, null=True)),
                ('status', models.CharField(max_length=25, null=True)),
                ('comments', models.CharField(max_length=300, null=True)),
                ('dar', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.dar', verbose_name='DAR')),
            ],
        ),
        migrations.AddField(
            model_name='dut',
            name='product_id',
            field=models.ForeignKey(db_column='product_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.product', verbose_name='Product'),
        ),
        migrations.CreateModel(
            name='DARChannel',
            fields=[
                ('channel_id', models.AutoField(primary_key=True, serialize=False)),
                ('channel_number', models.SmallIntegerField(null=True)),
                ('number_of_duts', models.SmallIntegerField(null=True)),
                ('power_supply_type', models.CharField(max_length=20, null=True)),
                ('power_supply_48V', models.SmallIntegerField(null=True)),
                ('power_supply_12V', models.SmallIntegerField(null=True)),
                ('max_current_48V', models.CharField(max_length=10, null=True)),
                ('max_current_12V', models.CharField(max_length=10, null=True)),
                ('power_supply_model', models.CharField(max_length=50, null=True)),
                ('eWP_Primary', models.CharField(max_length=3, null=True)),
                ('eWP_Med_Aux', models.CharField(max_length=3, null=True)),
                ('eTMOP', models.CharField(max_length=3, null=True)),
                ('eCF', models.CharField(max_length=3, null=True)),
                ('lin', models.CharField(max_length=5, null=True, verbose_name='LIN')),
                ('pwn', models.CharField(max_length=5, null=True, verbose_name='PWN')),
                ('can', models.CharField(max_length=5, null=True, verbose_name='CAN')),
                ('pressure_transducer_inlet', models.CharField(max_length=50, null=True)),
                ('pressure_transducer_outlet', models.CharField(max_length=50, null=True)),
                ('dar_id', models.ForeignKey(db_column='dar_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.dar', verbose_name='DAR')),
            ],
        ),
        migrations.AddField(
            model_name='dar',
            name='lab_id',
            field=models.ForeignKey(db_column='lab_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.lab', verbose_name='Lab'),
        ),
        migrations.CreateModel(
            name='ChamberLogInfo',
            fields=[
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pretest_inspection_and_photo', models.CharField(max_length=10, null=True, verbose_name='Pretest Inspection and Photo')),
                ('setup_photo', models.FloatField(null=True)),
                ('humidity', models.FloatField(null=True)),
                ('system_pressure', models.FloatField(null=True)),
                ('voltage', models.FloatField(null=True)),
                ('system_restriction_target', models.CharField(max_length=50, null=True)),
                ('system_restriction_record', models.CharField(max_length=10, null=True, verbose_name='System Restriction Record')),
                ('trial_run_record_and_process', models.CharField(max_length=10, null=True, verbose_name='Trial Run Record And Process')),
                ('special_requirements', models.CharField(max_length=300, null=True)),
                ('coolant', models.CharField(max_length=100, null=True)),
                ('temperature', models.FloatField(null=True)),
                ('test_profile', models.CharField(max_length=300, null=True)),
                ('shaker_profile', models.CharField(max_length=300, null=True)),
                ('chamber_profile', models.CharField(max_length=300, null=True)),
                ('pump_profile', models.CharField(max_length=300, null=True)),
                ('comments', models.CharField(max_length=4000, null=True)),
                ('chamber_id', models.ForeignKey(db_column='chamber_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.chamber', verbose_name='Chamber')),
                ('program_id', models.ForeignKey(db_column='program_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.program', verbose_name='Program')),
                ('technician_id', models.ForeignKey(db_column='technician_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.technician', verbose_name='Technician')),
                ('test_id', models.ForeignKey(db_column='test_id', on_delete=django.db.models.deletion.CASCADE, to='database.test', verbose_name='Test')),
            ],
        ),
        migrations.CreateModel(
            name='ChamberLog',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField()),
                ('circuit_number', models.SmallIntegerField()),
                ('total_hours', models.SmallIntegerField()),
                ('status', models.CharField(max_length=20, null=True, verbose_name='Status')),
                ('comments', models.CharField(max_length=300, null=True)),
                ('technician', models.CharField(max_length=100, null=True)),
                ('shaker_direction', models.CharField(max_length=100, null=True)),
                ('cage_id', models.ForeignKey(db_column='cage_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.cage', verbose_name='Cage')),
                ('chamber_id', models.ForeignKey(db_column='chamber_id', on_delete=django.db.models.deletion.CASCADE, to='database.chamber', verbose_name='Chamber')),
                ('dar_id', models.ForeignKey(db_column='dar_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='database.dar', verbose_name='DAR')),
                ('log_id', models.ForeignKey(db_column='log_id', on_delete=django.db.models.deletion.CASCADE, to='database.chamberloginfo', verbose_name='Log')),
            ],
        ),
        migrations.AddField(
            model_name='chamber',
            name='lab_id',
            field=models.ForeignKey(db_column='lab_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.lab'),
        ),
    ]
