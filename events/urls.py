from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('test/', test,name='test'),
    path('testid/<int:id>', testid,name='testid'),
    path('render/', renderlist,name='render'),
    path('eventlistvview/',ListEvent.as_view(),name='listeventview'),
    path('DetailEventView/<int:pk>/',DetailEventView.as_view(),name='DetailEventView'),
    #path('DetailEventView/<slug:slug>',DetailEventView.as_view(),name='DetailEventView')
    path('addevent/',add_event,name='add_event'),
    path('updateevent/<int:pk>/',UpdateView.as_view(),name='update_event')
    
]