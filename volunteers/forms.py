from django import forms
from .models import Volunteer
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class VolunteerForm(UserCreationForm):
    class Meta:
        model = Volunteer
        fields = [
            'username', 'first_name', 'last_name', 'email', 'password1', 'password2', 
            'phone', 'address', 'city', 'skills', 'availability', 'role'
        ]
    
    # Add help text for better user experience
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['role'].help_text = 'Select "Recruiter" if you are recruiting volunteers, otherwise choose "Volunteer".'
        self.fields['skills'].help_text = 'Describe your skills or expertise here.'

class VolunteerAuthForm(AuthenticationForm):
    class Meta:
        model = Volunteer
        fields = ['username', 'password1','password2'] 
