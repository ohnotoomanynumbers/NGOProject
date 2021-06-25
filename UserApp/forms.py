from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import CustomUser

class registeration_form(UserCreationForm):
    username = forms.CharField(max_length=32, help_text='username')
    firstName = forms.CharField(max_length=32, help_text='first name')
    lastName=forms.CharField(max_length=32, help_text='last name')
    email=forms.EmailField(max_length=32, help_text='email')
    password1=forms.CharField(max_length=32, help_text='password')
    password2=forms.CharField(max_length=32, help_text='password comfirm')
    role=forms.CharField(max_length=32, help_text='role')

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        # fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        fields = UserCreationForm.Meta.fields + ('firstName', 'lastName', 'email',)
