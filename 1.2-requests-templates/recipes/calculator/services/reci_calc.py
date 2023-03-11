DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    }


def get_recipe(food):
    if food in DATA:
        context = DATA.get(food)
        return context
    else:
        return None
    
def calculate_food(food,servings=1):
    recipe = {}
    for key, value in get_recipe(food).items():
        recipe[key] = value * int(servings)
    context = dict.fromkeys(['recipe'], recipe)
    print(context)
    return context
    


