from django.db import models
from django.conf import settings


import datetime
from django.contrib.auth.models import User

class food(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default='01-01-1002')
    # date = models.DateTimeField('date booked')

    breakfast = models.BooleanField(default=True)
    lunch = models.BooleanField(default=True)
    snacks = models.BooleanField(default=True)
    dinner = models.BooleanField(default=True)



