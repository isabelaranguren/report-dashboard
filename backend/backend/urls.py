
from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import upload_file, ClientViewSet

router = routers.DefaultRouter()
router.register(r'clients', ClientViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', upload_file, name='upload_file'),
] + router.urls



