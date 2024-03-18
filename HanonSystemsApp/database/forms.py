from django.forms import ModelForm
from .models import Program
from .models import Product
from .models import Test
from .models import ChamberLogInfo
from .models import ChamberLog
from django import forms
from django.utils import timezone
from datetime import datetime 


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
    supervisor_comments = forms.CharField(widget=forms.Textarea(attrs={"rows":"3"}))          
    class Meta:
        model = Test
        exclude = ('created', )
    def save(self, commit=True):
        
        instance = super(TestUpdateForm, self).save(commit=False) 
        if commit:
            instance.save()
            # self.save_m2m()
        ch = ChamberLogInfo.objects.get(test_id = instance.pk)
        print(datetime.now())
        o = ''
        if ch.comments in instance.supervisor_comments and ch.comments != instance.supervisor_comments:
            o = instance.supervisor_comments.replace(ch.comments, '')
            n = "\n"+str(datetime.now()) +" " + o
            new = ch.comments + n
            ch.comments = new
            instance.supervisor_comments = new
            instance.save()
            print(o)
        
        


        ch.chamber_id = instance.chamber_id
        ch.technician_id = instance.technician_id
        ch.program_id= instance.program_id
        ch.comments = instance.supervisor_comments


        ch.save()
        
            
            
        return instance

class TestForm(ModelForm):
    targeted_start = forms.DateField(
        widget = forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    targeted_end = forms.DateField(
        widget = forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    setup_date = forms.DateField(
        widget = forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    supervisor_comments = forms.CharField(widget=forms.Textarea(attrs={"rows":"3"}))        
    class Meta:
        model = Test
        exclude = ('created', )
    def save(self, commit=True):
        instance = super(TestForm, self).save(commit=False)
        if commit:
            instance.save()
            # self.save_m2m()
        print(str(instance.created) + instance.supervisor_comments)
        c = str(datetime.now()) + " "+ instance.supervisor_comments
        
        ch = ChamberLogInfo( chamber_id = instance.chamber_id, program_id = instance.program_id, technician_id = instance.technician_id, test_id = Test.objects.get(pk = instance.pk),
                                pretest_inspection_and_photo=None,
                                setup_photo=None,
                                humidity=None,
                                system_pressure=None,
                                voltage=None,
                                comments= c,
                                system_restriction_target=None,
                                system_restriction_record=None,
                                trial_run_record_and_process=None,
                                special_requirements=None)
        instance.supervisor_comments = c
        instance.save()
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
    comments = forms.CharField(widget=forms.Textarea(attrs={"rows":"3"}))  
    class Meta:
        model = ChamberLogInfo
        exclude = ('created', )
    def save(self, commit=True):
        instance = super(ChamberLogInfoForm, self).save(commit=False)
        if commit:
            instance.save()
            # self.save_m2m()
        print(instance.pk)
        ch = Test.objects.get(pk = instance.test_id.pk)

        o = instance.comments.replace(ch.supervisor_comments, '')
        n = "\n"+str(datetime.now()) +" " + o
        new = ch.supervisor_comments + n
        ch.supervisor_comments = new
        instance.comments = new
        instance.save()


        ch.chamber_id = instance.chamber_id
        ch.technician_id = instance.technician_id
        ch.program_id= instance.program_id


        ch.save()
        return instance



class ChamberLogForm(ModelForm):
    timestamp = forms.DateTimeField(input_formats = ['%Y-%m-%dT%H:%M'],
        widget = forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}))
    class Meta:
        model = ChamberLog
        fields = '__all__'


