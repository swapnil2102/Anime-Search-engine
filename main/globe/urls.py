from django.urls import path

from .import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('result/', views.anime_search, name='anime_search'),
    path('home/result/', views.anime_search, name='anime_search'),
    path('', views.home, name='home'),
    path('display/', views.display, name='display')

]