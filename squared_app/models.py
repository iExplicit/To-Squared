from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class HashTag(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)


class Squared(models.Model):
    title = models.CharField(max_length=50, blank=True)
    description = models.TextField(null=True,blank=True)
    done = models.BooleanField(default=False, blank=True)
    created_at = models.DateTimeField(default=timezone.now,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True)

    hashtags = models.ManyToManyField(HashTag)
