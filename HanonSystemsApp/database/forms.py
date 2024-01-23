from django.forms import ModelForm
from .models import Program
from .models import Product

# Create the form class.
class ProgramForm(ModelForm):
    class Meta:
        model = Program
        fields = '__all__'

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

