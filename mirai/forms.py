from django import forms
from mirai.models import DrugTest, Employee, SensorDetails, SensorRepairLog, TrackingLog
from mirai.models import Company

# This is for employee
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['eFname', 'eLname', 'eDepartment', 'eEmail', 'ePhone','eState', 'eCity','eZip']
        

#this is for company
class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = "__all__"

#this is for sensor details
class SensorDetailsForm(forms.ModelForm):
    class Meta:
        model = SensorDetails
        fields = ['sInstallationDate', 'sDepartment', 'sName', 'sFloor', 'sRoom','sDirection']

class RepairLogForm(forms.ModelForm):
    class Meta:
        model = SensorRepairLog
        fields = ['sDateDown','sDateRestored' ,'sTechnician', 'sCause', 'sRepaired']

class TrackingLogForm(forms.ModelForm):
    class Meta:
        model = TrackingLog
        fields = ['sID', 'eID', 'eAction']

class DrugTestForm(forms.ModelForm):
    class Meta:
        model = DrugTest
        fields = ['eID', 'labID', 'result', 'tDate', 'labTest']
        
#class loginForm(forms.ModelForm):
    #class Meta:
        #model = Login
        #fields = "__all__"