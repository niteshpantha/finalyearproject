from django.db import models


# Create your models here.


class Contact(models.Model):
    full_name = models.CharField("Full Name", max_length=50)
    email = models.EmailField("Email", max_length=150)
    address = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=150)
    message = models.TextField(max_length=200)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.full_name
