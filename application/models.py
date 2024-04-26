from django.db import models
from datetime import date


# Create your models here.

class enquiry_table(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=10)
    message = models.TextField()
    date_field = models.DateField(default=date.today)

    def __str__(self):
        return self.name



