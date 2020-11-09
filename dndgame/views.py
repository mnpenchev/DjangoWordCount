from django.shortcuts import render


def dndgame(request):
    return render(request, 'dnd_game.html')
