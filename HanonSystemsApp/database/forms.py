from django.forms import ModelForm
from .models import *
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
    date_inserted = forms.DateField(
        widget = forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    date_removed = forms.DateField(
        widget = forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), required=False)
    class Meta:
        model = Test_Harness
        exclude = ('created', )

class Test_DUTForm(ModelForm):
    date_inserted = forms.DateField(
        widget = forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    date_removed = forms.DateField(
        widget = forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), required=False)
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


# class TestUpdateForm(ModelForm):
#     targeted_start = forms.DateField(
#         widget = forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
#     targeted_end = forms.DateField(
#         widget = forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
#     supervisor_comments = forms.CharField(widget=forms.Textarea(attrs={"rows":"3"}))          
#     class Meta:
#         model = Test
#         exclude = ('created', )
#     def save(self, commit=True):
        
#         instance = super(TestUpdateForm, self).save(commit=False) 
#         #if commit:
#             #instance.save()
#             #self.save_m2m()
#         test = Test.objects.get(pk = instance.pk)

#         if test.supervisor_comments in instance.supervisor_comments and test.supervisor_comments != instance.supervisor_comments:
#             input = instance.supervisor_comments.replace("\n" + test.supervisor_comments, '')
#             new_line = str(datetime.now().date()) +" " + input + "\n"
#             new_comment = new_line +test.supervisor_comments
#             instance.supervisor_comments = new_comment
#             instance.save()
#         elif test.supervisor_comments == instance.supervisor_comments:
#             instance.save()
#         else:
#             position = instance.supervisor_comments.find("\n")
#             new_line = str(datetime.now().date()) +" "+ instance.supervisor_comments[:position+1]
#             new_comment = new_line + instance.supervisor_comments[position+1:]
#             instance.supervisor_comments = new_comment
#             instance.save()

#         info = ChamberLogInfo.objects.get(test_id = instance.pk)
#         info.comments = instance.supervisor_comments
#         info.chamber_id = instance.chamber_id
#         info.technician_id = instance.technician_id
#         info.program_id= instance.program_id
        
#         info.save()
            
            
#         return instance

# class TestForm(ModelForm):
#     targeted_start = forms.DateField(
#         widget = forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
#     targeted_end = forms.DateField(
#         widget = forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
#     supervisor_comments = forms.CharField(widget=forms.Textarea(attrs={"rows":"3"}), required=False)        
#     class Meta:
#         model = Test
#         exclude = ('created', )
#     def save(self, commit=True):
#         instance = super(TestForm, self).save(commit=False)
#         #if commit:
#             #instance.save()
#             # self.save_m2m()
#         print(instance.supervisor_comments)
#         print(type(instance.supervisor_comments))
#         if instance.supervisor_comments:
#             c = str(datetime.now().date()) + " "+ instance.supervisor_comments
#             instance.supervisor_comments = c
#             instance.save()
#         else:
#             instance.save()
#         ch = ChamberLogInfo( chamber_id = instance.chamber_id, program_id = instance.program_id, technician_id = instance.technician_id, test_id = Test.objects.get(pk= instance.pk),
#                                 pretest_inspection_and_photo=None,
#                                 setup_photo=None,
#                                 humidity=None,
#                                 system_pressure=None,
#                                 voltage=None,
#                                 comments= instance.supervisor_comments,
#                                 system_restriction_target=None,
#                                 system_restriction_record=None,
#                                 trial_run_record_and_process=None,
#                                 special_requirements=None)

#         ch.save() 
        
            
            
#         return instance


class TestUpdateForm(ModelForm):
    choices1 = ((None, '-----'),('complete', 'complete'),('cancelled', 'cancelled'),('current', 'current'),('upcoming', 'upcoming'),('archive', 'archive'),('next 1', 'next 1'),('next 2', 'next 2'),('next 3', 'next 3'),('next 4', 'next 4'),('next 5', 'next 5'),('next 6', 'next 6'),('next 7', 'next 7'),('next 8', 'next 8'),('next 9', 'next 9'),('next 10', 'next 10'))
    choices2 = ((None, '-----'),('0-stopped', '0-stopped'),('1-setup', '1-setup'),('2-running', '2-running'),('3-data review', '3-data review'),('4-on hold', '4-on hold'),('5-no man power', '5-no man power'),('6-on track', '6-on track'),)
    choices3 = ((None, '-----'),(1, 1),(2, 2),(3, 3),)
    targeted_start = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), required=False)
    targeted_end = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), required=False)
    supervisor_comments = forms.CharField(widget=forms.Textarea(attrs={"rows": "3"}), required=False)
    scheduling= forms.ChoiceField(
        widget=forms.Select,
        choices = choices1,
        required=False
    )
    status= forms.ChoiceField(
        widget=forms.Select,
        choices = choices2,
        required=False
    )
    priority= forms.ChoiceField(
        widget=forms.Select,
        choices = choices3,
        required=False
    )
    
    program_id = forms.ModelChoiceField(
        queryset= Program.objects.all(),
        required=False,
        label="Program")
    
    test_map_id = forms.ModelChoiceField(
        queryset= TestMap.objects.all(),
        required=False,
        label="Test Map")
    
    product_id = forms.ModelChoiceField(
        queryset= Product.objects.all(),
        required=False,
        label="Product")
    
    test_type_id = forms.ModelChoiceField(
        queryset= TestType.objects.all(),
        required=False,
        label="Test Type")
    
    test_description = forms.CharField(
        required=False,
        label="Test Description")
    
    technician_id = forms.ModelChoiceField(
        queryset= Technician.objects.all(),
        required=False,
        label="Technician")
    
    chamber_id = forms.ModelChoiceField(
        queryset= Chamber.objects.all(),
        required=False,
        label="Chamber")
    
    dar_id = forms.ModelChoiceField(
        queryset= DAR.objects.all(),
        required=False,
        label="DAR")
    
    cage_id = forms.ModelChoiceField(
        queryset= Cage.objects.all(),
        required=False,
        label="Cage")
    
    lab_id = forms.ModelChoiceField(
        queryset= Lab.objects.all(),
        required=False,
        label="Lab")
    
    hours_planned = forms.IntegerField(
        required=False,
        label="Hours Planned")
    
    total_hours = forms.IntegerField(
        required=False,
        label="Total Hours")

    class Meta:
        model = Test
        exclude = ('created',)


class TestForm(ModelForm):
    choices1 = ((None, '-----'),('complete', 'complete'),('cancelled', 'cancelled'),('current', 'current'),('upcoming', 'upcoming'),('archive', 'archive'),('next 1', 'next 1'),('next 2', 'next 2'),('next 3', 'next 3'),('next 4', 'next 4'),('next 5', 'next 5'),('next 6', 'next 6'),('next 7', 'next 7'),('next 8', 'next 8'),('next 9', 'next 9'),('next 10', 'next 10'))
    choices2 = ((None, '-----'),('0-stopped', '0-stopped'),('1-setup', '1-setup'),('2-running', '2-running'),('3-data review', '3-data review'),('4-on hold', '4-on hold'),('5-no man power', '5-no man power'),('6-on track', '6-on track'),)
    choices3 = ((None, '-----'),(1, 1),(2, 2),(3, 3),)
    targeted_start = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), required=False)
    targeted_end = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), required=False)
    supervisor_comments = forms.CharField(widget=forms.Textarea(attrs={"rows": "3"}), required=False)
    scheduling= forms.ChoiceField(
        widget=forms.Select,
        choices = choices1,
        required=False
    )
    status= forms.ChoiceField(
        widget=forms.Select,
        choices = choices2,
        required=False
    )
    priority= forms.ChoiceField(
        widget=forms.Select,
        choices = choices3,
        required=False
    )
    
    program_id = forms.ModelChoiceField(
        queryset= Program.objects.all(),
        required=False,
        label="Program")
    
    test_map_id = forms.ModelChoiceField(
        queryset= TestMap.objects.all(),
        required=False,
        label="Test Map")
    
    product_id = forms.ModelChoiceField(
        queryset= Product.objects.all(),
        required=False,
        label="Product")
    
    test_type_id = forms.ModelChoiceField(
        queryset= TestType.objects.all(),
        required=False,
        label="Test Type")
    
    test_description = forms.CharField(
        required=False,
        label="Test Description")
    
    technician_id = forms.ModelChoiceField(
        queryset= Technician.objects.all(),
        required=False,
        label="Technician")
    
    chamber_id = forms.ModelChoiceField(
        queryset= Chamber.objects.all(),
        required=False,
        label="Chamber")
    
    dar_id = forms.ModelChoiceField(
        queryset= DAR.objects.all(),
        required=False,
        label="DAR")
    
    cage_id = forms.ModelChoiceField(
        queryset= Cage.objects.all(),
        required=False,
        label="Cage")
    
    lab_id = forms.ModelChoiceField(
        queryset= Lab.objects.all(),
        required=False,
        label="Lab")
    
    hours_planned = forms.IntegerField(
        required=False,
        label="Hours Planned")
    
    total_hours = forms.IntegerField(
        required=False,
        label="Total Hours")

    
    class Meta:
        model = Test
        exclude = ('created',)

    def save(self, commit=True):
        instance = super(TestForm, self).save(commit=False)

        if instance.priority =='':
            instance.priority = None
        
        # 处理 supervisor_comments 字段
        if instance.supervisor_comments:
            c = str(datetime.now().date()) + " " + instance.supervisor_comments
            instance.supervisor_comments = c

        instance.save()

        ch = ChamberLogInfo(
            chamber_id=instance.chamber_id,
            program_id=instance.program_id,
            technician_id=instance.technician_id,
            test_id=Test.objects.get(pk=instance.pk),
            pretest_inspection_and_photo=None,
            setup_photo=None,
            humidity=None,
            system_pressure=None,
            voltage=None,
            comments=instance.supervisor_comments,
            system_restriction_target=None,
            system_restriction_record=None,
            trial_run_record_and_process=None,
            special_requirements=None
        )

        ch.save()

        return instance



class ChamberLogInfoForm(ModelForm):
    comments = forms.CharField(widget=forms.Textarea(attrs={"rows":"3"}))  
    class Meta:
        model = ChamberLogInfo
        exclude = ('created', )
    def save(self, commit=True):
        instance = super(ChamberLogInfoForm, self).save(commit=False)
        #if commit:
            #instance.save()
            # self.save_m2m()
        info = ChamberLogInfo.objects.get(pk = instance.pk)

        if info.comments in instance.comments and info.comments != instance.comments:
            input = instance.comments.replace("\n" + info.comments, '')
            new_line = str(datetime.now().date()) +" " + input + "\n"
            new_comment = new_line +info.comments
            instance.comments = new_comment
            instance.save()
        elif info.comments == instance.comments:
            instance.save()
        else:
            new_comment = str(datetime.now().date()) +" "+ instance.comments
            instance.comments = new_comment
            instance.save()

        test = Test.objects.get(pk = instance.test_id.pk)
        test.supervisor_comments = instance.comments
        test.chamber_id = instance.chamber_id
        test.technician_id = instance.technician_id
        test.program_id= instance.program_id


        test.save()
        return instance



class ChamberLogForm(ModelForm):
    timestamp = forms.DateTimeField(input_formats = ['%Y-%m-%dT%H:%M'],
        widget = forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}))
    class Meta:
        model = ChamberLog
        exclude = ('created', )
    def save(self, commit=True, *args, **kwargs):
        instance = super(ChamberLogForm, self).save(commit=False)
        
        if commit:
            instance.save()
            # self.save_m2m()
        ch = ChamberLogInfo.objects.get(pk= instance.log_id.pk)
        t = Test.objects.get(pk = ch.test_id.pk)
        try:
            if (int(instance.total_hours) > int(t.total_hours)):
                t.total_hours = instance.total_hours   
        except:
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
        
        
##################################################################################################################################################################

class FixturesForm(ModelForm):
    class Meta:
        model = Fixtures
        exclude = ('created', )
        
##################################################################################################################################################################