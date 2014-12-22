from django.db import models

# Create your models here.
class Entry(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)