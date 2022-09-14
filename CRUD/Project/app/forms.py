from django import forms
from . models import *
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    class meta:
        fields = ['username','password','password2']