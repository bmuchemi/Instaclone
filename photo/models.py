from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=500)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['?']
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_caption(self, new_caption):
        self.caption = new_caption
        self.save()

    def update_likes(self):
        self.likes += 1
        self.save()


   
    