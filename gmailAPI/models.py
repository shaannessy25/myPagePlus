from django.db import models

# Create your models here.
class GmailUser(models.Model):
    token = models.FileField(upload_to="secrets/")