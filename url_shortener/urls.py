from django.contrib import admin
from django.urls import path,include

from shorten_url.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shorten_url.urls')),
]
