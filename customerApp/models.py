from django.db import models

from UserApp import models as umod
from events import models as emod


class Address(models.Model):
    customer = models.ForeignKey(
        umod.CustomUser,
        on_delete=models.CASCADE
    )
    address1 = models.CharField(
        "Address line 1",
        max_length=1024,
    )
    address2 = models.CharField(
        "Address line 2",
        max_length=1024,
    )

    zip_code = models.CharField(
        "ZIP / Postal code",
        max_length=12,
    )
    city = models.CharField(
        "City",
        max_length=1024,
    )


class Customer(models.Model):
    customer = models.OneToOneField(
        umod.CustomUser,
        on_delete=models.CASCADE,
    )
    contact_num = models.CharField(max_length=10)
    address = Address()
    events = models.ManyToManyField(
        emod.Event,
    )
