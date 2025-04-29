#all root names for API
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [


] + static (settings.MEDIA.URL, document_root=settings.MEDIA_ROOT) #for uploed  from backend
