from django.urls import path
from . import views
urlpatterns = [
 
 path('qr', views.qr,name='qr'),


]