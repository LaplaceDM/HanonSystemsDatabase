from django.forms import ModelForm
from .models import Program
from .models import Product
from .models import Test
from .models import ChamberLogInfo
from .models import ChamberLog
from django import forms
from django.utils import timezone


# Create the form class.
class ProgramForm(ModelForm):
    class Meta:
        model = Program
        exclude = ('created', )

class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ('created', )


class TestUpdateForm(ModelForm):
    targeted_start = forms.DateField(
        widget = forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    targeted_end = forms.DateField(
        widget = forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    setup_date = forms.DateField(
        widget = forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))        
    class Meta:
        model = Test
        exclude = ('created', )
    def save(self, commit=True):
        instance = super(TestUpdateForm, self).save(commit=False)
        if commit:
            instance.save()
            # self.save_m2m()
        print(instance.pk)
        
        ch = ChamberLogInfo.objects.get(test_id = instance.pk)
        ch.chamber_id = instance.chamber_id
        ch.technician_id = instance.technician_id
        ch.program_id= instance.program_id
        print(instance.created)
        print(ch.created)
        print(ch.chamber_id)
        print(ch.program_id)
        print(ch.test_id)
        print(ch.technician_id)
        print(ch.voltage)
        print(ch.pk)
        print(ch.special_requirements)

        ch.save() 
        
            
            
        return instance

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
    def save(self, commit=True):
        instance = super(TestForm, self).save(commit=False)
        if commit:
            instance.save()
            # self.save_m2m()
        print(instance.pk)
        
        ch = ChamberLogInfo( chamber_id = instance.chamber_id, program_id = instance.program_id, technician_id = instance.technician_id, test_id = Test.objects.get(pk = instance.pk),
                                pretest_inspection_and_photo=None,
                                setup_photo=None,
                                humidity=None,
                                system_pressure=None,
                                voltage=None,
                                system_restriction_target=None,
                                system_restriction_record=None,
                                trial_run_record_and_process=None,
                                special_requirements=None)
        print(instance.created)
        print(ch.created)
        print(ch.chamber_id)
        print(ch.program_id)
        print(ch.test_id)
        print(ch.technician_id)
        print(ch.voltage)
        print(ch.pk)
        print(ch.special_requirements)

        ch.save() 
        
            
            
        return instance

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


