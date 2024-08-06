from django.db import models
from django.contrib.auth.models import User
# Create your models here.
GENDER_OPTIONS = {
    'M':'Male',
    'F':'Female'
}
CHEST_PAIN_OPTIONS = {
    'TA': 'Typical Angina',
    'ATA': 'Atypical Angina', 
    'NAP': 'Non-Anginal Pain', 
    'ASY': 'Asymptomatic'
}
BLOOD_SUGAR_OPTIONS = {
    '0':'Less than or equal to 120',
    '1':'More than to 120'
}

RESTING_ECG_OPTIONS = {
    'Normal': 'Normal', 
    'ST': 'having ST-T wave abnormality', 
    'LVH': "showing probable or definite left ventricular hypertrophy by Estes' criteria"
}

EXERCISE_ANGINA_OPTIONS = {
    'Y':'Yes',
    'N':'No'
}

ST_SLOPE_OPTIONS = {
    'Up': 'upsloping', 
    'Flat': 'flat', 
    'Down': 'downsloping'
}

APPOINTMENT_STATUS_OPTIONS = {
    'Booked':'Booked',
    'Visited':'Visited',
    'Canceled':'Canceled'
}
class Heartvital(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    Age = models.IntegerField()
    Sex = models.CharField(max_length=255,choices=GENDER_OPTIONS)
    ChestPainType = models.CharField(max_length=255,choices=CHEST_PAIN_OPTIONS,verbose_name='Chest Pain Type')
    RestingBP = models.IntegerField(verbose_name='Resting Blood Pressure (60-220)')
    Cholesterol = models.IntegerField()
    FastingBS = models.CharField(max_length=255,choices=BLOOD_SUGAR_OPTIONS,verbose_name='Fasting Blood Sugar (60-900)')
    RestingECG = models.CharField(max_length=255,choices=RESTING_ECG_OPTIONS,verbose_name='Resting ECG Condtion')
    MaxHR = models.IntegerField(verbose_name='Maximum Heart Rate (60-220)')
    ExerciseAngina = models.CharField(max_length=255,choices=EXERCISE_ANGINA_OPTIONS,verbose_name='Exercise Anginia')
    Oldpeak = models.FloatField(verbose_name='Oldpeak (-2.5 - +2.5)')
    ST_Slope = models.CharField(max_length=255,choices=ST_SLOPE_OPTIONS)
    HeartDisease = models.CharField(max_length=255,blank=True)
    prediction_probability = models.CharField(max_length=255,blank=True)

    def __str__(self):
        return self.user.username
    
class Appointment(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    mobile = models.CharField(max_length=20)
    date = models.DateField()
    note = models.TextField()
    status = models.CharField(max_length=255,choices=APPOINTMENT_STATUS_OPTIONS,default="Booked")

    def __str__(self):
        return self.user.first_name+" "+self.user.last_name
    
class Patient(models.Model):
    patient = models.OneToOneField(User,on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    background_history = models.TextField()

    def __str__(self):
        return self.patient.username
    def full_name(self):
        return f"{self.patient.first_name} {self.patient.last_name}"

class Visit(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    diagnosis = models.TextField()

    def __str__(self):
        return f"{self.created_at}"
