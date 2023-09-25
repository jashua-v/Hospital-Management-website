from django.shortcuts import render, redirect
from .models import Patient, Appointment

def home(request):
    return render(request, 'home.html')

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient_list.html', {'patients': patients})

def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointment_list.html', {'appointments': appointments})

def add_patient(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        patient = Patient(name=name, age=age, gender=gender, address=address)
        patient.save()
        return redirect('patient_list')
    return render(request, 'add_patient.html')

def add_appointment(request):
    if request.method == 'POST':
        patient_id = request.POST.get('patient')
        date = request.POST.get('date')
        time = request.POST.get('time')
        patient = Patient.objects.get(id=patient_id)
        appointment = Appointment(patient=patient, date=date, time=time)
        appointment.save()
        return redirect('appointment_list')
    patients = Patient.objects.all()
    return render(request, 'add_appointment.html', {'patients': patients})
