#import forms from django module
from django import forms
#import model class from models.py of clinicalsapp folder
from clinicalsapp.models import ClinicalData,Patient
#create form for doing CRUD operations for Patient data
class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields='__all__'
#creating form  for adding data and analyzing patient data
class ClinicalDataForm(forms.ModelForm):
    class Meta:
        model=ClinicalData
        fields='__all__'
