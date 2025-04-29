#connect urls.py//base to django project
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('base.urls')) #includes in project
]
