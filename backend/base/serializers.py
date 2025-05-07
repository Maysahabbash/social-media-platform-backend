from rest_framework import serializers
from .models import MyUser, Post

class UserRegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True) #  Ensures password is never returned in API responses

    class Meta:
        model = MyUser #Our custom user model
        fields = ['username', 'email', 'first_name', 'last_name', 'password']

    def create(self, validated_data):  # Custom user model
        user = MyUser(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password']) # Django’s built-in password hashing
        # Never stores raw password  
        user.save()
        return user

class MyUserProfileSerializer(serializers.ModelSerializer):

    follower_count = serializers.SerializerMethodField() 
    following_count = serializers.SerializerMethodField()

    class Meta:
        model = MyUser
        fields = ['username', 'bio', 'profile_image', 'follower_count', 'following_count']

    def get_follower_count(self, obj):# Count people following you
        return obj.followers.count()
    
    def get_following_count(self, obj):
        return obj.following.count() # Count people you follow
    

class PostSerializer(serializers.ModelSerializer):

    username = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    formatted_date = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'username', 'description', 'formatted_date', 'likes', 'like_count']

    def get_username(self, obj): #  Get author's name
        return obj.user.username
    
    def get_like_count(self, obj):
        return obj.likes.count() # Count likes
    
    def get_formatted_date(self, obj):
        return obj.created_at.strftime("%d %b %y")
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['username', 'bio', 'email', 'profile_image', 'first_name', 'last_name']