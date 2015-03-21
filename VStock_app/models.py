from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    balance = models.IntegerField(default=10000)
    stocks_owned = models.TextField(default="")
    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
# Create your models here.
