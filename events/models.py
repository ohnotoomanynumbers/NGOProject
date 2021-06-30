from django.db import models
# Create your models here.
from django.utils import timezone
from django.urls import reverse

EVENT_CHOICES =(
    ("Conference", "Conference"),
    ("Seminar", "Seminar"),
    ("Presentation", "Presentation"),
    )
class Event(models.Model):
    """
    class EventCategory(models.TextChoices):
        SEMINAR = 'Seminar'
        CONFERENCE = 'Conference'
        PRESENTATION = 'Presentation'

    name = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    category = models.CharField(
        max_length=12,
        choices=EventCategory.choices,
        default=EventCategory.PRESENTATION
    )
    """
    event_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices = EVENT_CHOICES)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    adult_price = models.FloatField()
    child_price = models.FloatField()
    event_description = models.CharField(max_length=200)
    event_image=models.ImageField(default="default.jpg", upload_to="event_image")
    allow_registration=models.BooleanField(default=True)

    def __str__(self):
        return self.event_name

    def get_absolute_url(self):
        return reverse("event-detail", kwargs={"pk": self.pk})

class EventRegisterInfo(models.Model):
    event_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.IntegerField()
    address = models.CharField(max_length=200)
    adult_qty = models.IntegerField()
    child_qty = models.IntegerField()

    def __str__(self):
        return self.email

