from django.contrib.auth.models import User
from django.db import models
from pytz import all_timezones


class LifeUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    timezone = models.CharField(max_length=30, choices=((tz, tz) for tz in all_timezones))
