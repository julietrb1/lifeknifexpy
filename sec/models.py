import pytz
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from pytz import all_timezones


class LifeUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    timezone = models.CharField(max_length=30, choices=((tz, tz) for tz in all_timezones))

    def get_current_time(self):
        return timezone.now().astimezone(
            pytz.timezone(self.timezone))
