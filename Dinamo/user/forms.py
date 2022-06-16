from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django import forms


class SignUpForm(UserCreationForm):
    '''Class to construct a custom sign up form -derived for UserCreatioForm'''

    first_name=forms.CharField(max_length=128)
    last_name=forms.CharField(max_length=128)
    email=forms.EmailField(max_length=128)

    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']


class ProfileForm(forms.ModelForm):
    '''Class to construct a form for Profile objects'''

    class Meta:
        model=Profile
        fields='__all__'

        