from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import MyUser
from .serializers import MyUserProfileSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.response import Response

class CustomTokenObtainPairView(TokenObtainPairView):

    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            
            # Check if parent class returned valid tokens
            if response.status_code != 200:
                return response

            tokens = response.data

            # Create response object FIRST
            res = Response({
                "success": True,
                "message": "Login successful"
            })
            
            # Set cookies on the response object
            res.set_cookie(
                key='access_token',
                value=tokens['access'],
                httponly=True,
                secure=True,
                samesite='None',
                path='/'
            )
            
            res.set_cookie(
                key='refresh_token',
                value=tokens['refresh'],
                httponly=True,
                secure=True,
                samesite='None',
                path='/'
            )
            
            return res  # Return the actual response object
            
        except Exception as e:
            # Log the error for debugging
            print(f"Error in token obtain: {str(e)}")
            return Response({'success': False, 'error': str(e)}, status=400)

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