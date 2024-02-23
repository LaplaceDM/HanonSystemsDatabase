from django.forms import ModelForm
from .models import Program
from .models import Product
from .models import Test
from .models import ChamberLogInfo
from .models import ChamberLog
from django import forms


# Create the form class.
class ProgramForm(ModelForm):
    class Meta:
        model = Program
        exclude = ('created', )

class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ('created', )

class TestForm(ModelForm):
    targeted_start = forms.DateField(
        widget = forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    targeted_end = forms.DateField(
        widget = forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    setup_date = forms.DateField(
        widget = forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))        
    class Meta:
        model = Test
        exclude = ('created', )

class ChamberLogInfoForm(ModelForm):
    class Meta:
        model = ChamberLogInfo
        exclude = ('created', )

class ChamberLogForm(ModelForm):
    timestamp = forms.DateTimeField(input_formats = ['%Y-%m-%dT%H:%M'],
        widget = forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}))
    class Meta:
        model = ChamberLog
        fields = '__all__'


