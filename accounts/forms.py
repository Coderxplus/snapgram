from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile
from django.contrib.auth.models import User



class UserForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control','id': 'password','placeholder': 'Enter password'}))
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class': 'form-control','id': 'username','placeholder': 'Enter username'}))
    email = forms.CharField(label="Email", widget=forms.TextInput(attrs={'class': 'form-control','id': 'username','placeholder': 'Enter username'}))
    class Meta:
        model = User
        fields = ["username", "password", "email"]


class ProfileForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','id': 'username','placeholder': 'Enter username'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','id': 'username','rows': 4,'placeholder': 'Enter username'}))
    profile_pic = forms.ImageField(widget=forms.ClearableFileInput(attrs={
        'class': 'form-control',
        'accept': 'image/*'
    }))

    class Meta:
        model = Profile
        fields = ["full_name", "bio", "profile_pic", ]

    