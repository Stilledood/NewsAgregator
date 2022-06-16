from django.db import models
from django.shortcuts import reverse,render
from django.contrib.auth.models import User,PermissionsMixin,BaseUserManager
from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(models.Model):
    '''Class to construct am model for user profile'''

    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='user_images',default='Dinamo-Logo.jpg')
    name=models.CharField(max_length=128)
    username=models.CharField(max_length=32)
    email_confirmed=models.BooleanField(default=False)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('profile_details',kwargs={'username':self.username})

    def get_update_url(self):
        return reverse('profile_update',kwargs={'username':self.username})


@receiver(post_save,sender=User)
def update_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
        
