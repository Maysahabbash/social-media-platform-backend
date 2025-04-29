from django.db import models

#create custom user modelSS
from django.contrib.auth.models import AbstractUser # this will Inherit Django's built-in user model

class MyUser (AbstractUser):
    username = models.CharField(max_length=50, unique=True, primary_key=True)
        #Username is the primary key (no default auto-increment ID)

    bio = models.CharField(max_length=500) 
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    #list of followers: users can have many followers
    follower = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True) 
    
    def __str__(self):
        return self.username # Display username in admin panel
    
