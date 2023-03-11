from django.shortcuts import render
from calculator.services.reci_calc import calculate_food


def calculator(request, food):
        servings = request.GET.get('servings',1)
        return render(request, 'calculator/index.html', calculate_food(food, servings))

