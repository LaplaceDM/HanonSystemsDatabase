from django.forms import ModelForm
from .models import Program
from .models import *
from .models import Test
from .models import ChamberLogInfo
from .models import ChamberLog
from .models import Cage
from .models import DAR
from .models import Chamber
from django import forms
from django.utils import timezone
from datetime import datetime 
from dal import autocomplete


# Create the form class.
class ProgramForm(ModelForm):
    class Meta:
        model = Program
        exclude = ('created', )

class LaptopForm(ModelForm):
    class Meta:
        model = Laptop
        exclude = ('created', )

class Test_HarnessForm(ModelForm):
    class Meta:
        model = Test_Harness
        exclude = ('created', )

class Test_DUTForm(ModelForm):
    class Meta:
        model = Test_DUT
        exclude = ('created', )

class Technician_SkillForm(ModelForm):
    class Meta:
        model = Technician_Skill
        exclude = ('created', )

class TestMapForm(ModelForm):
    class Meta:
        model = TestMap
        exclude = ('created', )

class Test_ChamberForm(ModelForm):
    class Meta:
        model = Test_Chamber
        exclude = ('created', )



class Program_CageForm(ModelForm):
    class Meta:
        model = Program_Cage
        exclude = ('created', )

class Program_DARForm(ModelForm):
    class Meta:
        model = Program_DAR
        exclude = ('created', )

class Program_FluidForm(ModelForm):
    class Meta:
        model = Program_Fluid
        exclude = ('created', )

class DARChannelForm(ModelForm):
    class Meta:
        model = DARChannel
        exclude = ('created', )

class HarnessForm(ModelForm):
    class Meta:
        model = Harness
        exclude = ('created', )

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        exclude = ('created', )

class LabForm(ModelForm):
    class Meta:
        model = Lab
        exclude = ('created', )

class TestTypeForm(ModelForm):
    class Meta:
        model = TestType
        exclude = ('created', )

class TechnicianForm(ModelForm):
    class Meta:
        model = Technician
        exclude = ('created', )

class FluidForm(ModelForm):
    class Meta:
        model = Fluid
        exclude = ('created', )


class CageForm(ModelForm):
    class Meta:
        model = Cage
        exclude = ('created', )

class DarForm(ModelForm):
    class Meta:
        model = DAR
        exclude = ('created', )

class ChamberForm(ModelForm):
    class Meta:
        model = Chamber
        exclude = ('created', )

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


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
        #print(instance.created)
        #print(ch.created)
        #print(ch.chamber_id)
        #print(ch.program_id)
        #print(ch.test_id)
        #print(ch.technician_id)
        #print(ch.voltage)
        #print(ch.pk)
        #print(ch.special_requirements)

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
        exclude = ('', )
    def save(self, commit=True, *args, **kwargs):
        instance = super(ChamberLogForm, self).save(commit=False)
        
        if commit:
            instance.save()
            # self.save_m2m()
        print(instance.pk)
        ch = ChamberLogInfo.objects.get(pk= instance.log_id.pk)
        t = Test.objects.get(pk = ch.test_id.pk)
        if (instance.total_hours > t.total_hours):
            t.total_hours = instance.total_hours      
        t.save()
        instance.save()
        return instance


class DUTForm(ModelForm):
    received_date = forms.DateField(
        widget = forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    storage_date = forms.DateField(
        widget = forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    class Meta:
        model = DUT
        exclude = ('created', )
        
class SubcomponentForm(ModelForm):
    class Meta:
        model = Subcomponent
        exclude = ('component_id',)
        
class DAR_ChannelForm(ModelForm):
    class Meta:
        model = DARChannel
        exclude = ('channel_id', )