from django.urls import path
from . import views

urlpatterns = [
    path('', views.shorten_url,name="shorten_url"),
    path('<str:short_url>', views.getOriginalUrl, name="get_orijiginal_url")
  
  
]