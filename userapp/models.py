from django.db import models

# Create your models here.
from django.db import models

from django.db import models

class TblRegister(models.Model):
    STATUS_CHOICES = [
        ("approved", "Approved"),
        ("blocked", "Blocked"),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    profile = models.ImageField(upload_to="profiles/", null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="approved")  # Added status field

    def __str__(self):
        return self.name

