from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import EventManageView, EventListView, EventCreateView, EventUpdateView, EventDeleteView, EventDetailView, EventRegisterView


urlpatterns = [
    path('', views.EventListView.as_view(), name="events-list"),
    path('events/manage/', views.EventManageView.as_view(), name="events-manage"),
    path('events/create/', views.EventCreateView.as_view(), name="events-create"),
    path('events/<int:event_pk>/event_register/', views.EventRegisterView.as_view(), name="event-register"),
    path("events/<int:pk>/detail/", views.EventDetailView.as_view(), name="event-detail"),
    path("events/<int:pk>/delete/", views.EventDeleteView.as_view(), name="events-delete"),
    path("events/<int:pk>/update/", views.EventUpdateView.as_view(), name="events-update"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
