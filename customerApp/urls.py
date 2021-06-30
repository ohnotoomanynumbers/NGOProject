from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.EventListView.as_view(), name="home"),
    path("<int:pk>/", views.EventDetailView.as_view(), name='event-detail'),
    path("<int:pk>/register", views.EventRegisterView.as_view(), name='event-register')
]