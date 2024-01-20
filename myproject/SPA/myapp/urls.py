from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
   #path('admin/', admin.site.urls),
    path('hello1/', hello1, name='hello'),
    path('',myhome, name='myhome'),
     path('deals/',mydeals, name='mydeals'),
    path('skin/', skincare, name='skincare'),
path('buynow/',buynow, name='buynow'),
path('login/', login, name='login'),
    path('signup/', signup, name='signup'),

    ]