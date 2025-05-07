from django.db import models
# Import the base user model to extend
from django.contrib.auth.models import AbstractUser

# Custom user model extending Django's AbstractUser
class MyUser(AbstractUser):
     # Unique username serving as primary identifier
    username = models.CharField(max_length=50, unique=True, primary_key=True)
    bio = models.CharField(max_length=500)
    profile_image = models.ImageField(upload_to='profile_image/', blank=True, null=True)  # Profile picture storage
    # Social follow system (many-to-many relationship)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)
    # Users can follow other users
    # Following isn't mutual by default
    # Can have zero followers
    def __str__(self):
        return self.username
# Post model for user-generated content
class Post(models.Model):
        # User who made this post
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='posts')# Delete posts when user is deleted
    description = models.CharField(max_length=400)
# Post creation date/time (auto-filled)
    created_at = models.DateTimeField(auto_now_add=True)
    # Users who liked this post
    likes = models.ManyToManyField(MyUser, related_name='post_likes', blank=True)



