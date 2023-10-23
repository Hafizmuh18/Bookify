from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class CustomUser(AbstractUser):
    ROLES = (
        ('member', 'Member'),
        ('moderator', 'Moderator')
    )
    role = models.CharField(max_length=10, choices=ROLES, default='member')

class Book(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, null=True, blank=True)
    book = models.TextField()
