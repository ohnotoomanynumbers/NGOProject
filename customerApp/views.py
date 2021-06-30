from django.views.generic import ListView, DetailView

from .models import Customer
from events.models import Event


class EventListView(ListView):
    model = Event
    template_name = "customer_home.html"
    context_object_name = "cevents"


class EventDetailView(DetailView):
    model = Event
    template_name = "customer_event_detail.html"
    context_object_name = "cdetail"

