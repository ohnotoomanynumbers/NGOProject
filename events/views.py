from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import event_create_form, event_update_form, event_register_form

from .models import *
# Create your views here.
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect


class EventManageView(LoginRequiredMixin, ListView):
    model = Event
    template_name = "events/events_manage.html"
    context_object_name = "events"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if not request.user.role == "admin":
                return HttpResponseForbidden()
        else:
            return HttpResponseForbidden()
        return super().dispatch(request, *args, **kwargs)

class EventListView(ListView):
    model = Event
    template_name = "events/events_list.html"
    context_object_name = "events"

class EventCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Event
    template_name = "events/event_create.html"
    #fields = ["event_name", "category", "location", "start_date", "end_date", "start_time", "end_time", "adult_price", 
    #"child_price", "event_description", "event_image" ]
    form_class = event_create_form

class EventRegisterView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = EventRegisterInfo
    template_name = "events/event_register.html"
    form_class = event_register_form
    #queryset = Event.objects.all()
    #def form_valid(self, form):
    #    form.instance.event_name = get_object_or_404(Event, pk=self.kwargs.get('pk')).event_name
    #    return super(EventRegisterView, self).form_valid(form)
    """
    def form_valid(self, form):
        form.instance.event_name = Event.objects.get(pk=self.kwargs.get('pk'))
        return super().form_valid(form)
    """
    
    def form_valid(self, form):
        event_pk = self.kwargs['event_pk']
        event = get_object_or_404(Event, pk=event_pk)
        event_name = event.event_name
        self.object = form.save(commit=False)
        self.object.event_name = event_name
        self.object.save()
        return super(EventRegisterView, self).form_valid(form)
    
    """
    def get_context_data(self, **kwargs):
        context = super(EventRegisterView, self).get_context_data(**kwargs)
        context['listid']= self.kwargs['listid']
        return context
    """

class EventUpdateView(LoginRequiredMixin, UpdateView):
    model = Event
    form_class = event_update_form
    template_name = 'events/event_update.html'
    context_object_name = 'event'

    def get_success_url(self):
        return reverse_lazy('events-list')

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
    template_name = "events/event_delete.html"

    def get_success_url(self):
        return reverse('events-list')

class EventDetailView(DetailView):
    model = Event
    template_name = "events/event_detail.html"
    success_url = "/event_register/"
    def get_success_url(self):
        return reverse_lazy('event-register', kwargs={'event': self.object})