from django.db import models
from django import forms
class signup(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    email= forms.EmailField(label='Email',min_length=5)
    password = forms.CharField(widget=forms.PasswordInput())
    phone=forms.IntegerField(max_value=9999999999,min_value=6000000000)