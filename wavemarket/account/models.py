from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(max_length=13)
    discount = models.IntegerField(default=0)
    address = models.ForeignKey('Address',on_delete=models.SET_NULL,blank=True, null=True)
    photo = models.ImageField(upload_to='user_photo', blank=True, null=True)

    def __str__(self):
        return self.username

class Address(models.Model):
    country = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    address1 = models.CharField(max_length=250)
    address2 = models.CharField(max_length=250, null=True, blank=True)
    zipcode = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.country}, {self.state}, {self.city}, {self.address1}, {self.address2}, {self.zipcode}"
    
