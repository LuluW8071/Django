
from django.urls import path, include
from django.contrib import admin
from BetterDevice import views
from django.contrib.auth import views as auth_views 

urlpatterns=[
    path('admin/'  ,admin.site.urls, name='admin'),
    path('',views.LaptopListView.as_view(),name='laptop-list'),
    path('create',views.LaptopCreateView.as_view(),name='laptop-create'),
    path('<int:pk>/update',views.LaptopUpdateView.as_view(),name='laptop-update'),
    path('<int:pk>/delete',views.LaptopDeleteView.as_view(),name='laptop-delete'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='userapp/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="userapp/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='userapp/password_reset_complete.html'), name='password_reset_complete'),
] 
