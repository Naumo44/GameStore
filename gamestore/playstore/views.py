from django.shortcuts import render

categories = ['Аркады', 'Шутеры', 'Песочницы', 'RPG/MMO RPG',
            'Карточные игры', 'Файтинги', 'Гоночные симуляторы']

def index(request):
    games = ['Тачки', 'Срачки', 'NFS Unbound']
    context = {'cats': categories,
               'three_games': games}
    return render(request, 'playstore/index.html', context=context)

def show_game(request, name):
    context = {
        'name': name
	 }
    return render(request, 'playstore/game.html', context=context)

def show_all_categories(request):
    context = {
        'cats': categories,
        'games': ['Бутырка', 'Бутырка', 'Четырка', 'Чепырка', 'Аня Дыркина 3']
	 }
    return render(request, 'playstore/categories.html', context=context)