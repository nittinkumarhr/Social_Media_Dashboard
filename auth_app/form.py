from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from user.models import User
# from django.contrib.auth.models import  User


class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=('full_name','email','username','password1','password2',)
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=User
        fields=('full_name','email','username')