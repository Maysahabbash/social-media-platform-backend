from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import MyUser
from .serializers import MyUserProfileSerializer


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