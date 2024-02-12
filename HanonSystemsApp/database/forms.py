from django.forms import ModelForm
from .models import Program
from .models import Product
from .models import Test
from django import forms


# Create the form class.
class ProgramForm(ModelForm):
    class Meta:
        model = Program
        fields = '__all__'

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

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


