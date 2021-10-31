from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE

# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Advisor(models.Model):
    name = models.CharField(max_length=255)
    profileUrl = models.CharField(max_length=255)


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    advisor = models.ForeignKey(Advisor, on_delete=CASCADE)
    bookingTime = models.DateTimeField(auto_now=True)
