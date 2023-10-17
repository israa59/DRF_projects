from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    bio = models.TextField(blank=True)
    display_picture = models.ImageField()