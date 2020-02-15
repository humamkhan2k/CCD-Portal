from django import forms
from django.forms import ModelForm
from .models import UserProfile,StudentsAnnouncement
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('company','email')
        
class StudentsAnnouncmentForm(forms.ModelForm):
    class Meta:
        model = StudentsAnnouncement
        fields = ('student','rollnumber','Announcement')