from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# create model class named Patient
class Patient(models.Model):
    lastName=models.CharField(max_length=20)
    firstName=models.CharField(max_length=20)
    age=models.IntegerField()
    def __str__(self):
        return f'{self.firstName} {self.lastName}'
#create model class named ClinicalData
#Relationship from Patient to ClinicalData is one to many
#In patient model class,auto generated id is primary-key and it acts 
#as foreignkey for ClinicalData model class
class  ClinicalData(models.Model):
    #componentName is a dropdown on the UI
    #hw,bp,heartrate are dropdown value and Height/Weight,Blood Pressure,Heart Rate' are values display on screen.
    COMPONENT_NAMES=[('hw','Height/Weight'),('bp','Blood Pressure'),
                     ('heartrate','Heart Rate')]
    componentName=models.CharField(choices=COMPONENT_NAMES,max_length=20)
    componentValue=models.CharField(max_length=20)
    #for current date and time , we use auto_now_add=True
    measuredDateTime=models.DateTimeField(auto_now_add=True)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
# class Clinicsuser(models.Model):
#     user=models.OneToOneField(User, on_delete=models.CASCADE)
#     nickname=models.CharField(max_length=20,null=False)

