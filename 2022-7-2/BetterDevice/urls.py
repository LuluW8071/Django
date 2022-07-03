
from django.urls import path, include
from django.contrib import admin
from BetterDevice import views

urlpatterns=[
    path('admin/'  ,admin.site.urls, name='admin'),
    path('',views.LaptopListView.as_view(),name='laptop-list'),
    path('create',views.LaptopCreateView.as_view(),name='laptop-create'),
    path('<int:pk>/update',views.LaptopUpdateView.as_view(),name='laptop-update'),
    path('<int:pk>/delete',views.LaptopDeleteView.as_view(),name='laptop-delete'),
] 
