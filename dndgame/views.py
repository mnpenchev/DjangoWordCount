from django.shortcuts import render

fighter = {'name': 'Korgan', 'attack_num': 3, 'attack_dice': 20, 'max_health': 250, 'health': 250, 'AC': 15, 'init': 16,
           'experience': 0, 'gold': 0, 'level': 1}
mage = {'name': 'Edwin', 'attack_num': 2, 'attack_dice': 15, 'max_health': 200, 'health': 200, 'AC': 12, 'init': 10,
        'experience': 0, 'gold': 0, 'level': 1}
cleric = {'name': 'Viconia', 'attack_num': 1, 'attack_dice': 15, 'max_health': 120, 'health': 120, 'AC': 12, 'init': 11,
          'experience': 0, 'gold': 0, 'level': 1}
rogue = {'name': 'Yoshimo', 'attack_num': 4, 'attack_dice': 15, 'max_health': 100, 'health': 100, 'AC': 14, 'init': 18,
         'experience': 0, 'gold': 0, 'level': 1}


def dndgame(request):
    return render(request, 'dnd_game.html')


def choose_hero(request):
    hero = int(request.GET['bb'])
    if hero == 1:
        player_class = fighter
        return render(request, 'game_on.html', {'hero': fighter})

    if hero == 2:
        player_class = mage
        return render(request, 'game_on.html', {'hero': mage})

    if hero == 3:
        player_class = cleric
        return render(request, 'game_on.html', {'hero': cleric})

    if hero == 4:
        player_class = rogue
        return render(request, 'game_on.html', {'hero': rogue})


def game_on(request):
    pass

