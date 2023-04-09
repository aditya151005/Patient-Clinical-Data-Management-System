from django.shortcuts import render,redirect
#import model class from models.py of clinicalsapp folder
#using Patient model class, We can perform CRUD operations on
# patient data using class based view
from clinicalsapp.models import ClinicalData,Patient
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
#import different types of view
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
#importing clinicalDataForm
from clinicalsapp.forms import ClinicalDataForm
# Create your views here.
#Restrict access to the unauthenticated users 
@method_decorator(login_required(login_url='/clinicalsapp/login/'), name='dispatch')
class PatientListView(ListView):
    model=Patient
#Restrict access to the unauthenticated users 
@method_decorator(login_required(login_url='/clinicalsapp/login/'), name='dispatch')    
class PatientCreateView(CreateView):
    model=Patient
    success_url=reverse_lazy('index')
    fields=('firstName','lastName','age')
#Restrict access to the unauthenticated users 
@method_decorator(login_required(login_url='/clinicalsapp/login/'), name='dispatch')
class PatientUpdateView(UpdateView):
    model=Patient
    success_url=reverse_lazy('index')
    fields=('firstName','lastName','age')
#Restrict access to the unauthenticated users 
@method_decorator(login_required(login_url='/clinicalsapp/login/'), name='dispatch')
class PatientDeleteView(DeleteView):
    model=Patient
    success_url=reverse_lazy('index') 
#Adding clinical data
#Restrict access to the unauthenticated users  
@login_required(login_url='/clinicalsapp/login/')
def addData(request,**kwargs):
    form=ClinicalDataForm()  
    patient=Patient.objects.get(id=kwargs['pk'])
    if request.method=='POST':
        form=ClinicalDataForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/clinicalsapp/patientlist')
    return render(request,'clinicalsapp/clinicaldata_form.html',{'form':form,'patient':patient})

#Analyzing clinical data
#Restrict access to the unauthenticated users 
@login_required(login_url='/clinicalsapp/login/')
def analyze(request,**kwargs):
    data=ClinicalData.objects.filter(patient_id=kwargs['pk'])
    patient=Patient.objects.get(id=kwargs['pk'])
    responseData=[]
    for eachEntry in data:
        if eachEntry.componentName=='hw':
            heightAndWeight=eachEntry.componentValue.split('/')
            if len(heightAndWeight)>1:
                feetToMetres=float(heightAndWeight[0])*0.4536
                BMI=(float(heightAndWeight[1]))/(feetToMetres*feetToMetres)
                bmiEntry=ClinicalData()
                bmiEntry.componentName='BMI'
                bmiEntry.componentValue=BMI
                responseData.append(bmiEntry)
        responseData.append(eachEntry)
    return render(request,'clinicalsapp/generate_report.html',{'data':responseData,'patient':patient})
# user login view
def userLogin(request):
    data = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect('/clinicalsapp/patientlist')
        else:
            data['error'] = 'username or password is incorrect'
            res = render(request, 'clinicalsapp/user_login.html', data)
            return res
    else:
        res = render(request, 'clinicalsapp/user_login.html', data)
        return res
# user logout view
def userLogout(request):
    logout(request)
    return HttpResponseRedirect('/clinicalsapp/login/')
