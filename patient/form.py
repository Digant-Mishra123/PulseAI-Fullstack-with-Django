from django.forms import ModelForm
from django import forms
from patient.models import Heartvital
from django.contrib.auth.models import User

class HeartVitalForm(ModelForm):
    class Meta:
        model = Heartvital
        # fields = '__all__'
        exclude = ['user','HeartDisease','prediction_probability']

class EmailChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']