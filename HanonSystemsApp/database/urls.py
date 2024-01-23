from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProgramListView.as_view(), name="index"),
    path("product", views.ProductListView.as_view(), name="product"),
    path("product/delete_item/<int:pk>", views.delete_item_product, name="delete_product"),
    path("product/update/<int:pk>", views.UpdateTableViewProduct.as_view(), name="update_product"),
    # path("delete", views.DeleteProgramListView.as_view(), name="delete"),
    path('delete_item/<int:pk>', views.delete_item, name="delete_item"),
    path('update/<int:pk>', views.UpdateTableView.as_view(), name="update"),
    # path("add", views.home_view, name="add")
]

