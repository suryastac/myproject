from django.db import models

# Create your models here.
class UserDetails(models.Model):
    userID = models.CharField(max_length=255)
    password = models.CharField(max_length=255)