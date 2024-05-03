from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,get_user_model,password_validation


class RegForm(UserCreationForm):
    password1=forms.CharField(
        label=("password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete":"new password","class":"form-control"}),
        help_text=("Enter the same password as before for verification "),
    )
    password2=forms.CharField(
        label=("password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new password","class":"form-control"}),
        help_text=password_validation.password_validators_help_text_html(),
     )
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]
        widgets={
            'first_name':forms.TextInput(attrs={"class":"form-control"}),
            'last_name':forms.TextInput(attrs={"class":'form-control'}),
            'email':forms.EmailInput(attrs={"class":'form-control'}),
            'username':forms.TextInput(attrs={"class":'form-control'}),
        }


class LogForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100,widget=forms.PasswordInput())

