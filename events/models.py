from django.db import models

# Create your models here.
from django.utils import timezone



class Event(models.Model):

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
    start = models.DateTimeField()
    end = models.DateTimeField()
    adult_price = models.FloatField()
    discount_price = models.FloatField()
