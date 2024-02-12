from django.urls import path
from . import views

urlpatterns = [
    path("program", views.ProgramListView.as_view(), name="index"),
    path("product", views.ProductListView.as_view(), name="product"),
    path("product/delete_item/<int:pk>", views.delete_item_product, name="delete_product"),
    path("product/update/<int:pk>", views.UpdateTableViewProduct.as_view(), name="update_product"),
    # path("delete", views.DeleteProgramListView.as_view(), name="delete"),
    path('program/delete_item/<int:pk>', views.delete_item, name="delete_program"),
    path('program/update/<int:pk>', views.UpdateTableView.as_view(), name="update_program"),
    # path("add", views.home_view, name="add")
    path("tests", views.TestListView.as_view(), name="test"),
    path("tests/delete_item/<int:pk>", views.delete_item_test, name="delete_test"),
    path("tests/update/<int:pk>", views.UpdateTableViewTest.as_view(), name="update_test"),
    path("tests/clone/<int:pk>", views.clone_item, name="clone"),
    path("children", views.children, name="children"),
    path("getchildren", views.getchildren, name="getchildren"),
    path("darchildren", views.darchildren, name="darchildren"),
    path("getdarchildren", views.getdarchildren, name="getdarchildren"),
]

