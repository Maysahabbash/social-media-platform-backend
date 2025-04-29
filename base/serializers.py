from rest_framework import serializers
from .models import MyUser

class MyUserProfileSerializer(serializers.ModelSerializer):

    follower_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField ()
    class Meta:
     model = MyUser
     fields = ['username', 'bio', 'profile_image', 'follower_count', 'following_count']

    # Method to get follower count

     def get_follower_count(self, obj):
        return obj.followers.count()# Count users following this user
    # Method to get following count

     def get_following_count(self, obj):
        return obj.following.count()# Count users following this user
