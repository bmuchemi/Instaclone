from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=500)
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

