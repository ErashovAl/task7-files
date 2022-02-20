from pprint import pprint
import os

def recipes():
    path = os.path.join(os.getcwd(), 'recipe.txt')
    with open(path, encoding='utf8') as data:
        cook_book = {}
        for line in data:
            dish_name = line.strip()
            cook_book[dish_name] = []
            count = int(data.readline())
            
            for x in range(count):
                ingredient, quantity, measure = data.readline().split('|')
                cook_book[dish_name].append(
                        {'ingredient_name': ingredient, 'quantity':quantity, 'measure': measure.strip()}
                                            )
            data.readline()
    return cook_book

# pprint(recipes(), width=100, sort_dicts = False)

def get_shp_l(dishes, person, recipe=recipes()):
    total = {}
   
    for dish in dishes:
        if dish in recipe:
            for products in recipe[dish]:
                if products['ingredient_name'] not in total:
                    temp = {'quantity': int(products['quantity'])*person, 'measure': products['measure']}
                    total[products['ingredient_name']] = temp
                else:
                    total[products['ingredient_name']]['quantity'] += int(products['quantity'])*person
        else: return 'Такого блюда нет в книге'
    return total

pprint(get_shp_l(['Запеченный картофель','Омлет'], 2))