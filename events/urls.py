from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('', views.EventListView.as_view(), name="events-list"),
    path('manage/', views.EventManageView.as_view(), name="events-manage"),
    path('create/', views.EventCreateView.as_view(), name="events-create"),
    path('<int:event_pk>/event_register/', views.EventRegisterView.as_view(), name="event-register"),
    path("<int:pk>/detail/", views.EventDetailView.as_view(), name="event-detail"),
    path("<int:pk>/delete/", views.EventDeleteView.as_view(), name="events-delete"),
    path("<int:pk>/update/", views.EventUpdateView.as_view(), name="events-update"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
