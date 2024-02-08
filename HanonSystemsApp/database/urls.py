from django.urls import path
from . import views

urlpatterns = [
    path("program", views.ProgramListView.as_view(), name="program"),
    path('program/delete_program/<int:pk>', views.delete_program, name="delete_program"),
    path('program/update_program/<int:pk>', views.UpdateTableViewProgram.as_view(), name="update_program"),

    path("product", views.ProductListView.as_view(), name="product"),
    path("product/delete_product/<int:pk>", views.delete_item_product, name="delete_product"),
    path("product/update_product/<int:pk>", views.UpdateTableViewProduct.as_view(), name="update_product"),

    path("tests", views.TestListView.as_view(), name="test"),
    path("tests/delete_test/<int:pk>", views.delete_item_test, name="delete_test"),
    path("tests/update_test/<int:pk>", views.UpdateTableViewTest.as_view(), name="update_test"),
    path("tests/clone/<int:pk>", views.clone_item, name="clone"),

    path("chamberschedule", views.chamber_schedule, name ='chamberschedule'),
    path("getchamberschedule", views.get_chamber_schedule, name ='getchamberschedule'),
    path("darschedule", views.dar_schedule, name ='darschedule'),
    path("getdarschedule", views.get_dar_schedule, name ='getdarschedule'),
    path("cageschedule", views.cage_schedule, name ='cageschedule'),
    path("getcageschedule", views.get_cage_schedule, name ='getcageschedule'),
]


