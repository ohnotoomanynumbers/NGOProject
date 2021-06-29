from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
User = get_user_model()
"""
class registeration_form(UserCreationForm):
    email=forms.EmailField(max_length=999, help_text='email')
    username = forms.CharField(max_length=150, help_text='username')
    firstName = forms.CharField(max_length=40, help_text='first name')
    lastName=forms.CharField(max_length=40, help_text='last name')
    role=forms.CharField(max_length=40, help_text='role')
    password1=forms.CharField(max_length=999, help_text='password')
    password2=forms.CharField(max_length=999, help_text='password comfirm')

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        # fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        fields = UserCreationForm.Meta.fields + ("email", "username", 'firstName', 'lastName', 'role', "password1", "password2")
"""
ROLE_CHOICES =(
    ("admin", "admin"),
    ("user", "user"),
    )
class registeration_form(forms.ModelForm):
    #email=forms.EmailField(max_length=999, help_text='email')
    #username = forms.CharField(max_length=150, help_text='username')
    #firstName = forms.CharField(max_length=40, help_text='first name')
    #lastName=forms.CharField(max_length=40, help_text='last name')
    #role=forms.CharField(max_length=40, help_text='role')
    #password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    #role = forms.ChoiceField(choices = ROLE_CHOICES)
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'firstName', 'lastName',  "role")
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        #if role=="admin":
        #    user.is_staff=True
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    

class updateUser_form(forms.ModelForm):
    #email=forms.EmailField(max_length=999, help_text='email')
    #username = forms.CharField(max_length=150, help_text='username')
    #firstName = forms.CharField(max_length=40, help_text='first name')
    #lastName=forms.CharField(max_length=40, help_text='last name')
    #role=forms.CharField(max_length=40, help_text='role')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    #role = forms.ChoiceField(choices = ROLE_CHOICES)
    #password = ReadOnlyPasswordHashField()
    """
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        # fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        fields = UserCreationForm.Meta.fields + ("email", "username",'firstName', 'lastName', 'role', "password1", "password2")
    """
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'firstName', 'lastName', "role", 'is_active')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        #if role=="admin":
        #    user.is_staff=True
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user