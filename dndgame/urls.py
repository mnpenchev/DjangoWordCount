from django.urls import path
from dndgame import views

urlpatterns = [
    path('dndgame/', views.dndgame, name='dndgame'),
    path('choose_hero/', views.choose_hero, name='choose_hero'),
]
