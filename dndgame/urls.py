from django.urls import path
from dndgame import views

urlpatterns = [
    path('dndgame/', views.dndgame, name='dndgame'),
]
