from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=500)
    profile = models.ForeignKey(User, on_delete=models.CASCADE,default='')
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

    @classmethod    
    def get_user_images(cls, user_id):
        ''' method to retrieve all images'''
        img = Image.objects.filter(profile=user_id).all()
        sort = sorted(img, key=lambda t: t.created_at)
        return sort

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='avatars/', default='default.jpg')
    bio = models.TextField(default=f'Hello,I am new to instagram', blank=True)

    def __str__(self):
        return f'{self.use.username}'

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
    
    def update_bio(self, new_bio):
        self.bio = new_bio
        self.save()

    def update_photo(self, new_image, user_id):
        user = User.objects.get(id = user_id)
        self.photo = new_image
        self.save()

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    
   
    