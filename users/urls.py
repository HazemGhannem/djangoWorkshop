from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import *


urlpatterns = [
    path('login/',signIn,name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('signup/',signup,name='signup'),
]