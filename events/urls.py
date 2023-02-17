from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('test/', test,name='test'),
    path('testid/<int:id>', testid,name='testid'),
    path('render/', renderlist,name='render'),
    
]