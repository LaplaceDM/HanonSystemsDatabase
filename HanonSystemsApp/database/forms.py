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
        fields = '__all__' 


class TestFilterForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Assuming model name as "model", if it really is that you might want to change it
        self.fields['test_map_id'].queryset = Test.objects.none()
        if 'program_id' in self.data:
            try:
                program_id = int(self.data.get('program_id'))
                self.fields['test_map_id'].queryset = Test.objects.filter(program_id=program_id)
            except (ValueError, TypeError):
                pass

