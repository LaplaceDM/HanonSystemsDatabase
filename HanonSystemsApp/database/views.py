from django.shortcuts import render
from database.models import *

# Create your views here.
def index(request):
    queryset = Program.objects.all()
    return render(request, "html/test3.html", {"queryset": queryset})