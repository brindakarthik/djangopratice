from django.urls import path

from .views import *

urlpatterns=[
    path('',index,name='index'),
path('uploadresume',uploadresume,name='uploadresume'),
path('calculate',calculate,name='calculate'),
path('register',register,name='register'),
path('save',save,name='save'),
    path('retrieve',retrieve,name='retrieve'),
    path('login',login,name='login'),
    path('checklogin',checklogin,name='checklogin'),
    path('welcome',welcome,name='welcome'),
    path('product',product,name='product'),
path('editproduct',editproduct,name='editproduct'),
path('saveproduct',saveproduct,name='saveproduct'),
    path('addproduct',addproduct,name='addproduct'),
    path('searchproduct',searchproduct,name='searchproduct'),
    path('updateproduct',updateproduct,name='updateproduct'),
    path('deleteproduct',deleteproduct,name='deleteproduct'),
]