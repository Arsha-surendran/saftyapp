from django import forms
from .models import UserProfile,PoliceProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['address', 'phone', 'dob', 'location',  'profile_image', 'guardian_name', 'guardian_phone']



class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()


class PoliceProfileForm(forms.ModelForm):
    class Meta:
        model = PoliceProfile
        fields = ['station_name','officer_details','police_station_location','helpline_number']
