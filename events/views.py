from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import *
# Create your views here.
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect


class EventListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = "events/adevents_list.html"
    context_object_name = "events"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if not request.user.role == "admin":
                return HttpResponseForbidden()
        else:
            return HttpResponseForbidden()
        return super().dispatch(request, *args, **kwargs)


class EventCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Event
    template_name = "events/adcreate_event.html"
    #form_class = event_form

    def get_success_url(self):
        return reverse('events-list')


class EventUpdateView(LoginRequiredMixin, UpdateView):
    model = Event
    #form_class = updateEvent_form
    template_name = 'events/adevent_update.html'
    context_object_name = 'event'

    def get_success_url(self):
        return reverse('events-list')

    def form_valid(self, form):
        event = form.save(commit=True)
        event.save()
        return HttpResponseRedirect(self.get_success_url())

    def dispatch(self, request, *args, **kwargs):
        if not request.user.role=="admin":
            raise PermissionDenied()
        return super().dispatch(request, *args, **kwargs)

class EventDeleteView(LoginRequiredMixin, DeleteView):
    model = Event
    template_name = "events/adevent_delete.html"

    def get_success_url(self):
        return reverse('events-list')
