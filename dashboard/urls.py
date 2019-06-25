from django.contrib import admin
from django.urls import path, include


from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('detect', views.detect, name='detect'),


    #flower info
    path('sunflower/', views.sunflower, name='sunflower'),
    path('rose/', views.rose, name='rose'),
    path('daisy/', views.daisy, name='daisy'),
    path('dandelion/', views.dandelion, name='dandelion'),
    path('tulip/', views.tulip, name='tulip'),

]

