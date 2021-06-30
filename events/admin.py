from django.contrib import admin

# Register your models here.
<<<<<<< HEAD
from .models import Event
admin.site.register(Event)
=======
from events.models import Event

admin.site.register(Event)
>>>>>>> b4f590de32087a73108599623d12c68a008cb234
