from django.urls import path

from .views import *

urlpatterns=[
   path('',index,name='index'),
path('calculate/',calculate,name='calculate')
]