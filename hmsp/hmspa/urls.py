from django.urls import path
from hmspa import views

urlpatterns = [
    path('patients/', views.patient_list, name='patient_list'),
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('patients/add/', views.add_patient, name='add_patient'),
    path('appointments/add/', views.add_appointment, name='add_appointment'),
]
