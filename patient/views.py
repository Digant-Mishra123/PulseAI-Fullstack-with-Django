from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import datetime
from patient.models import Heartvital,Appointment,Visit,Patient
from patient.form import HeartVitalForm,EmailChangeForm
from patient.predict import predict_heart_disease
# Create your views here.
def signup(request):
    if request.method == "POST":
        fn = request.POST.get("f_name")
        ln = request.POST.get("l_name")
        un = request.POST.get("u_name")
        email = request.POST.get("email")
        pwd = request.POST.get("pass")

        # print(fn)
        if User.objects.filter(username=un).exists():
            messages.error(request,"Username is already taken")
        elif User.objects.filter(email=email).exists():
            messages.error(request,'Email is already taken')
        else:
            user = User.objects.create_user(
                first_name=fn,last_name=ln,username=un,email=email,password=pwd
            )
            user.save()
            messages.success(request,"Account created Successfully")
    return render(request,'patient/signup.html')

def signin(request):
    if request.method == "POST":
        username = request.POST.get("u_name")
        password = request.POST.get("pass")

        user=authenticate(request,username=username,password=password)
        if user is None:
            messages.error(request,"Invalid Username or Password")
        else:
            # messages.error(request, "You required to sign in to take the test")
            login(request,user)
            return redirect('home')
    return render(request,'patient/signin.html')


def signout(request):
    logout(request)
    return redirect('home')

@login_required(login_url='signin')
def take_a_test(request):
    context = {}
    today = timezone.now().date()
    today = datetime.today()
    is_exists = Heartvital.objects.filter(user=request.user, created_at__date=today).count()
    if( is_exists > 0):
        context["error"] = True

    form = HeartVitalForm()
    if request.method == "POST":
        form = HeartVitalForm(request.POST)
        # print(form.data)
        patient = form.save(commit=False)
        # Prediction
        patient_data = {}
        for k, v in form.data.items():
            patient_data[k] = v
        patient_data.pop('csrfmiddlewaretoken')
        print(patient_data)
        prediction = predict_heart_disease(patient_data)
        print(prediction)
        context['prediction'] = prediction

        #save to database
        patient.user = request.user
        patient.heart_disease = prediction.get('class')
        patient.prediction_probability = prediction.get('probability')
        patient.save()

    context['form'] = form
        
    
    return render(request, 'patient/take_a_test.html', context)

@login_required(login_url='signin')
def appointment(request):
    if request.method == 'POST':
        mobile = request.POST.get('mobile')
        date = request.POST.get('date')
        note = request.POST.get('note')

        if Appointment.objects.filter(user=request.user,date=date).exists():
            messages.error(request, f"Appointment for {date} is already done")
        elif Appointment.objects.filter(date=date).count() >= 20:
            messages.error(request,f"All the slots of {date} is already booked")
        else:
            appointment = Appointment(user=request.user, mobile=mobile,date=date,note=note)
            appointment.save()
            messages.success(request,"Appointment Booked")

    appointments = Appointment.objects.filter(user=request.user).order_by("-date")
    context = {
        'appointments':appointments
    }
    return render(request,'patient/appointment.html',context)

def delete_appointment(request,aid):
    app = Appointment.objects.filter(id=aid).delete()
    if app:
        messages.success(request,"Appointment Deleted")
    else:
        messages.error(request,"Something Went Wrong")
    return redirect('appointment')


def update_appointment(request,aid):
    if request.method == 'POST':
        mobile = request.POST.get('mobile')
        date = request.POST.get('date')
        note = request.POST.get('note')

        if Appointment.objects.filter(user=request.user,date=date).exclude(id=aid).exists():
            messages.error(request, f"Appointment for {date} is already done")
        elif Appointment.objects.filter(date=date).count() >= 20:
            messages.error(request,f"All the slots of {date} is already booked")
        else:
            appointment = Appointment(id=aid, user=request.user, mobile=mobile,date=date,note=note)
            appointment.save()
            messages.success(request,"Appointment Updated")
            return redirect('appointment')
    app = Appointment.objects.get(id=aid)
    context = {
        'appointment':app
    }
    return render(request,'patient/appointment_update.html',context)

def profile(request):
    heart_vitals = Heartvital.objects.filter(user=request.user).order_by("-created_at")
    # patient = Patient.objects.get(patient=request.user)
    visits = {}
    if Patient.objects.filter(patient=request.user).exists():
        patient = Patient.objects.get(patient=request.user)
        visits = Visit.objects.filter(patient=patient)
    context = {
        'heart_vitals':heart_vitals,
        'visits':visits
    }

    return render(request,'patient/profile.html',context)

@login_required
def email_update(request):
    if request.method == "POST":
        email_form = EmailChangeForm(request.POST, instance=request.user)
        if email_form.is_valid():
            email_form.save()
            return redirect('profile')  # Redirect to the profile page after successful email change
    else:
        email_form = EmailChangeForm(instance=request.user)

    return render(request, 'patient/email_update.html', {'email_form': email_form})