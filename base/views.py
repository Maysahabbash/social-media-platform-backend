# Create your views here.
# Created function based views from django REST framework
# Create try except if the user doesn't exist

from .models import MyUser
from .serializers import MyUserProfileSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def get_user_profile_data(request, pk):
    try:
        try:
            user = MyUser.objects.get(username=pk)
        except MyUser.DoesNotExist:
            return Response({'error': 'user does not exsit'})

        serializer = MyUserProfileSerializer(user, many=False)
        return Response(serializer.data)
    except Exception:
        return Response({'error': 'error getting user data'})