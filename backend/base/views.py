from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import MyUser
from .serializers import MyUserProfileSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        tokens = response.data

        access_token = tokens ['access']
        refresh_token = tokens['refresh']

        res = Response()
        res = {"success":True}
        res.set_cookie(
           key = 'access_token',
           value=access_token,
           httponly = True,
           secure = True,
           samesite='None',
           path='/'

        )
        res.set_cookie(
           key = 'refresh_token',
           value=refresh_token,
           httponly = True,
           secure = True,
           samesite='None',
           path='/'

        )
        return res



# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile_data(request, pk):
    try:
        try:
            user = MyUser.objects.get(username=pk)
        except MyUser.DoesNotExist:
            return Response({'error':'user does not exist'})
        
        serializer = MyUserProfileSerializer(user, many=False)

        return Response(serializer.data)
    except:
        return Response({'error':'error getting user data'})