from django.db import models
from django.contrib.auth import User

# Create your models here.
class GmailUser(models.Model):
    
    token = models.FileField(upload_to="secrets/")