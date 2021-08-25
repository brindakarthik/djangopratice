from django.urls import path

from .views import *

urlpatterns=[
   # path('',index,name='index'),
path('calculate/',calculate,name='calculate'),
path('register/',register,name='register'),
path('save/',save,name='save'),
    path('retrieve',retrieve,name='retrieve')
]