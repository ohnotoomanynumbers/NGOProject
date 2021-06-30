
from django import forms
from .models import Event, EventRegisterInfo


class event_create_form(forms.ModelForm):
    #email=forms.EmailField(max_length=999, help_text='email')
    #username = forms.CharField(max_length=150, help_text='username')
    #firstName = forms.CharField(max_length=40, help_text='first name')
    #lastName=forms.CharField(max_length=40, help_text='last name')
    #role=forms.CharField(max_length=40, help_text='role')
    #password = forms.CharField(widget=forms.PasswordInput)
    #role = forms.ChoiceField(choices = ROLE_CHOICES)
	start_date=forms.DateField(help_text='example: 2021-1-25')
	end_date=forms.DateField(help_text='example: 2021-1-26')
	start_time=forms.TimeField(help_text='example: 14:30:00')
	end_time=forms.TimeField(help_text='example: 15:30:00')
	event_description = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'size':80}))
	class Meta:
		model = Event
		fields = ["event_name", "category", "location", "start_date", "end_date", "start_time", 
		"end_time", "adult_price", "child_price", "event_description", "event_image", "allow_registration"]

class event_update_form(forms.ModelForm):
	start_date=forms.DateField(help_text='example: 2021-1-25')
	end_date=forms.DateField(help_text='example: 2021-1-26')
	start_time=forms.TimeField(help_text='example: 14:30:00')
	end_time=forms.TimeField(help_text='example: 15:30:00')
	event_description = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'size':80}))
	class Meta:
		model = Event
		fields = ["event_name", "category", "location", "start_date", "end_date", "start_time", 
		"end_time", "adult_price", "child_price", "event_description", "event_image", "allow_registration"]

class event_register_form(forms.ModelForm):
	event_name = forms.CharField(max_length=100)
	first_name = forms.CharField(max_length=100)
	last_name = forms.CharField(max_length=100)
	email = forms.CharField(max_length=100)
	contact = forms.IntegerField()
	address = forms.CharField(max_length=200)
	adult_qty = forms.IntegerField()
	child_qty = forms.IntegerField()

	class Meta:
		model = Event
		fields = ["event_name", "first_name", "last_name", "email", "contact", "address", 
		"adult_qty", "child_qty"]
