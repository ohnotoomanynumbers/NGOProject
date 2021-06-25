from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import CustomUser

class registeration_form(UserCreationForm):
    email=forms.EmailField(max_length=32, help_text='email')
    username = forms.CharField(max_length=32, help_text='username')
    firstName = forms.CharField(max_length=32, help_text='first name')
    lastName=forms.CharField(max_length=32, help_text='last name')
    role=forms.CharField(max_length=32, help_text='role')
    password1=forms.CharField(max_length=32, help_text='password')
    password2=forms.CharField(max_length=32, help_text='password comfirm')

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        # fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        fields = UserCreationForm.Meta.fields + ('firstName', 'lastName', 'email',)
