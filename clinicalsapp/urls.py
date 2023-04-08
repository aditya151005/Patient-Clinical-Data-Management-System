from clinicalsapp import views
from django.urls import re_path, path
urlpatterns = [
    path('login/',views.userLogin),
    path('logout/',views.userLogout),
    path('patientlist/',views.PatientListView.as_view(),name='index'),
    path('create/',views.PatientCreateView.as_view()),
    path('update/<int:pk>/',views.PatientUpdateView.as_view()),
    path('delete/<int:pk>/',views.PatientDeleteView.as_view()),
    path('addData/<int:pk>/',views.addData),
    path('analyze/<int:pk>/',views.analyze),
]