from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('<str:name>', views.show_game, name='game'),
    path('categories/', views.show_all_categories, name='categories')
]