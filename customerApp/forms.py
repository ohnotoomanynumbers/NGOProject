from django.forms import ModelForm
from customerApp.models import Customer


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['firstName','lastName', 'email', 'contact_num', 'address']
