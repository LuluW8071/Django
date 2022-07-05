from nturl2path import url2pathname
from django.urls import path,include
from userapp import views
from django.contrib import admin

urlpatterns = [
    #path('',views.home, name='home'),
    path('register/',views.register,name="register"),
    path('login/',views.user_login,name= 'user-login'),
    path('logout/',views.user_logout,name='user-logout'),
    path("password_reset",views.password_reset_request,name="password_reset"),

    
]

