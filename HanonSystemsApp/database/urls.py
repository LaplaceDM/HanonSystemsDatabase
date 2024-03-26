from django.urls import path
from . import views

urlpatterns = [

    path("", views.menu, name="menu"),

    path("program", views.ProgramListView.as_view(), name="program"),
    path('program/delete_program/<int:pk>', views.delete_program, name="delete_program"),
    path('program/update_program/<int:pk>', views.UpdateTableViewProgram.as_view(), name="update_program"),
    path("program/clone/<int:pk>", views.clone_item2, name="clone2"),


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
    path("hours_download", views.hours_download, name = "hours download")
]


