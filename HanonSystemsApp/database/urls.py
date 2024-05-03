from django.urls import path
from . import views
from django.urls import re_path as url
from .models import Test
from dal import autocomplete

urlpatterns = [

    path("", views.menu, name="menu"),

    path("program", views.ProgramListView.as_view(), name="program"),
    path('program/delete_program/<int:pk>', views.delete_program, name="delete_program"),
    path('program/update_program/<int:pk>', views.UpdateTableViewProgram.as_view(), name="update_program"),
    path("program/clone/<int:pk>", views.clone_item2, name="clone2"),

    path("cage", views.CageListView.as_view(), name="cage"),
    path('cage/delete_cage/<int:pk>', views.delete_cage, name="delete_cage"),
    path('cage/update_cage/<int:pk>', views.UpdateTableViewCage.as_view(), name="update_cage"),

    path("Dar", views.DarListView.as_view(), name="Dar"),
    path('Dar/delete_Dar/<int:pk>', views.delete_Dar, name="delete_Dar"),
    path('Dar/update_Dar/<int:pk>', views.UpdateTableViewDar.as_view(), name="update_Dar"),

    path("Chamber", views.ChamberListView.as_view(), name="Chamber"),
    path('Chamber/delete_Chamber/<int:pk>', views.delete_Chamber, name="delete_Chamber"),
    path('Chamber/update_Chamber/<int:pk>', views.UpdateTableViewChamber.as_view(), name="update_Chamber"),

    path("Laptop", views.LaptopListView.as_view(), name="Laptop"),
    path('Laptop/delete_Laptop/<int:pk>', views.delete_Laptop, name="delete_Laptop"),
    path('Laptop/update_Laptop/<int:pk>', views.UpdateTableViewLaptop.as_view(), name="update_Laptop"),

    path("Test_Harness", views.Test_HarnessListView.as_view(), name="Test_Harness"),
    path('Test_Harness/delete_Test_Harness/<int:pk>', views.delete_Test_Harness, name="delete_Test_Harness"),
    path('Test_Harness/update_Test_Harness/<int:pk>', views.UpdateTableViewTest_Harness.as_view(), name="update_Test_Harness"),
    
    path("Test_DUT", views.Test_DUTListView.as_view(), name="Test_DUT"),
    path('Test_DUT/delete_Test_DUT/<int:pk>', views.delete_Test_DUT, name="delete_Test_DUT"),
    path('Test_DUT/update_Test_DUT/<int:pk>', views.UpdateTableViewTest_DUT.as_view(), name="update_Test_DUT"),

    path("Technician_Skill", views.Technician_SkillListView.as_view(), name="Technician_Skill"),
    path('Technician_Skill/delete_Technician_Skill/<int:pk>', views.delete_Technician_Skill, name="delete_Technician_Skill"),
    path('Technician_Skill/update_Technician_Skill/<int:pk>', views.UpdateTableViewTechnician_Skill.as_view(), name="update_Technician_Skill"),

    path("TestMap", views.TestMapListView.as_view(), name="TestMap"),
    path('TestMap/delete_TestMap/<int:pk>', views.delete_TestMap, name="delete_TestMap"),
    path('TestMap/update_TestMap/<int:pk>', views.UpdateTableViewTestMap.as_view(), name="update_TestMap"),

    path("Test_Chamber", views.Test_ChamberListView.as_view(), name="Test_Chamber"),
    path('Test_Chamber/delete_Test_Chamber/<int:pk>', views.delete_Test_Chamber, name="delete_Test_Chamber"),
    path('Test_Chamber/update_Test_Chamber/<int:pk>', views.UpdateTableViewTest_Chamber.as_view(), name="update_Test_Chamber"),

    path("Program_Cage", views.Program_CageListView.as_view(), name="Program_Cage"),
    path('Program_Cage/delete_Program_Cage/<int:pk>', views.delete_Program_Cage, name="delete_Program_Cage"),
    path('Program_Cage/update_Program_Cage/<int:pk>', views.UpdateTableViewProgram_Cage.as_view(), name="update_Program_Cage"),

    path("Program_DAR", views.Program_DARListView.as_view(), name="Program_DAR"),
    path('Program_DAR/delete_Program_DAR/<int:pk>', views.delete_Program_DAR, name="delete_Program_DAR"),
    path('Program_DAR/update_Program_DAR/<int:pk>', views.UpdateTableViewProgram_DAR.as_view(), name="update_Program_DAR"),

    path("Program_Fluid", views.Program_FluidListView.as_view(), name="Program_Fluid"),
    path('Program_Fluid/delete_Program_Fluid/<int:pk>', views.delete_Program_Fluid, name="delete_Program_Fluid"),
    path('Program_Fluid/update_Program_Fluid/<int:pk>', views.UpdateTableViewProgram_Fluid.as_view(), name="update_Program_Fluid"),

    path("DARChannel", views.DARChannelListView.as_view(), name="DARChannel"),
    path('DARChannel/delete_DARChannel/<int:pk>', views.delete_DARChannel, name="delete_DARChannel"),
    path('DARChannel/update_DARChannel/<int:pk>', views.UpdateTableViewDARChannel.as_view(), name="update_DARChannel"),

    path("Harness", views.HarnessListView.as_view(), name="Harness"),
    path('Harness/delete_Harness/<int:pk>', views.delete_Harness, name="delete_Harness"),
    path('Harness/update_Harness/<int:pk>', views.UpdateTableViewHarness.as_view(), name="update_Harness"),

    path("Skill", views.SkillListView.as_view(), name="Skill"),
    path('Skill/delete_Skill/<int:pk>', views.delete_Skill, name="delete_Skill"),
    path('Skill/update_Skill/<int:pk>', views.UpdateTableViewSkill.as_view(), name="update_Skill"),

    path("Lab", views.LabListView.as_view(), name="Lab"),
    path('Lab/delete_Lab/<int:pk>', views.delete_Lab, name="delete_Lab"),
    path('Lab/update_Lab/<int:pk>', views.UpdateTableViewLab.as_view(), name="update_Lab"),

    path("TestType", views.TestTypeListView.as_view(), name="TestType"),
    path('TestType/delete_TestType/<int:pk>', views.delete_TestType, name="delete_TestType"),
    path('TestType/update_TestType/<int:pk>', views.UpdateTableViewTestType.as_view(), name="update_TestType"),

    path("Technician", views.TechnicianListView.as_view(), name="Technician"),
    path('Technician/delete_Technician/<int:pk>', views.delete_Technician, name="delete_Technician"),
    path('Technician/update_Technician/<int:pk>', views.UpdateTableViewTechnician.as_view(), name="update_Technician"),

    path("Fluid", views.FluidListView.as_view(), name="Fluid"),
    path('Fluid/delete_Fluid/<int:pk>', views.delete_Fluid, name="delete_Fluid"),
    path('Fluid/update_Fluid/<int:pk>', views.UpdateTableViewFluid.as_view(), name="update_Fluid"),



    path("product", views.ProductListView.as_view(), name="product"),
    path("product/delete_product/<int:pk>", views.delete_item_product, name="delete_product"),
    path("product/update_product/<int:pk>", views.UpdateTableViewProduct.as_view(), name="update_product"),
    path("product/clone/<int:pk>", views.clone_item1, name="clone1"),

    path("tests", views.TestListView.as_view(), name="test"),
    path("tests/delete_test/<int:pk>", views.delete_item_test, name="delete_test"),
    path("tests/update_test/<int:pk>", views.UpdateTableViewTest.as_view(), name="update_test"),
    path("tests/clone/<int:pk>", views.clone_item, name="clone"),

    path("children", views.children, name="children"),
    path("children1", views.children1, name="children1"),
    path("getchildren", views.getchildren, name="getchildren"),
    path("darchildren", views.darchildren, name="darchildren"),
    path("getdarchildren", views.getdarchildren, name="getdarchildren"),

    path("short", views.short, name="short"),
    path("getshort", views.getshort, name="getshort"),


    path("chamberschedule", views.chamber_schedule, name ='chamberschedule'),
    path("getchamberschedule", views.get_chamber_schedule, name ='getchamberschedule'),
    path("darschedule", views.dar_schedule, name ='darschedule'),
    path("getdarschedule", views.get_dar_schedule, name ='getdarschedule'),
    path("cageschedule", views.cage_schedule, name ='cageschedule'),
    path("getcageschedule", views.get_cage_schedule, name ='getcageschedule'),
    
    path("ChamberLogInfo", views.ChamberLogInfoListView.as_view(), name="ChamberLogInfo"),
    path('ChamberLogInfo/delete_ChamberLogInfo/<int:pk>', views.delete_item_ChamberLogInfo, name="delete_ChamberLogInfo"),
    path('ChamberLogInfo/update_ChamberLogInfo/<int:pk>', views.UpdateTableViewChamberLogInfo.as_view(), name="update_ChamberLogInfo"),
    path("ChamberLogInfo/clone/<int:pk>", views.clone_item3, name="clone3"),

    path("find/<int:pk>", views.find, name="find"),

    path("ChamberLog/<int:pk>", views.ChamberLogView.as_view(), name="ChamberLog"),
    path('ChamberLog/delete_ChamberLog/<int:pk>', views.delete_item_ChamberLog, name="delete_ChamberLog"),
    # path('ChamberLog/update_ChamberLog/<int:pk>', views.UpdateTableViewChamberLog.as_view(), name="update_ChamberLog"),
    path("ChamberLog/clone/<int:pk>", views.clone_item4, name="clone4"),

    path("hourscalculations", views.hours_calculations, name= "hours calculations"),
    path("calculate", views.calculate, name = "calculate"),
    path("hours_download", views.hours_download, name = "hours download"),
    
    path("harness<int:id>", views.harness_info, name = "harness_info"),
    
    path("menu", views.menu, name = "menu"),
    
    path("dut", views.DUTListView.as_view(), name="dut"),
    path("dut/delete_dut/<int:pk>", views.delete_item_dut, name="delete_dut"),
    path("dut/update_dut/<int:pk>", views.UpdateTableViewDUT.as_view(), name="update_dut"),
    
    path("dut<int:pk>", views.DUTInfo.as_view(), name = "dut_info"),
    path("subcomponent/delete_subcomponent/<int:pk>", views.delete_item_subcomponent, name="delete_subcomponent"),
    path("subcomponent/update_subcomponent/<int:pk>", views.UpdateTableViewSubcomponent.as_view(), name="update_subcomponent"),
    
    path("dar_channel", views.DAR_ChannelListView.as_view(), name="DAR_Channel"),
    path("dar_channel/delete_dar_channel/<int:pk>", views.delete_DAR_Channel, name="delete_DAR_Channel"),
    path("dar_channel/update_dar_channel/<int:pk>", views.UpdateTableView_DAR_Channel.as_view(), name="update_DAR_Channel"),
]


