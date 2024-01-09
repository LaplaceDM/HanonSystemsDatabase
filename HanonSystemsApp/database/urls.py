from django.urls import path
from . import views

urlpatterns = [
    path("<str:name>", views.index, name="index")
]


#this is a test message
