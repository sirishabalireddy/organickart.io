from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class chef(models.Model):
    user = models.ForeignKey(User)
