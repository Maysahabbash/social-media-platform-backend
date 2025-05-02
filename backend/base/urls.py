
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import get_user_profile_data,CustomTokenObtainPairView, CustomTokenTokenRefreshView


from rest_framework_simplejwt.views import (
    
     TokenObtainPairView,

    TokenRefreshView,
)

urlpatterns = [
    path('user_data/<str:pk>/', get_user_profile_data),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenTokenRefreshView.as_view(), name='token_refresh'),



    
] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
