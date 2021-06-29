
from django.forms import ModelForm
from events.models import Event


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

class EventUpdateForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
