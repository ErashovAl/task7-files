from pprint import pprint
import os

# образец
#    cook_book = {
    #   'Омлет': [
    #     {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    #     {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    #     {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    #     ],
    #   'Утка по-пекински': [
    #     {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    #     {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    #     {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    #     {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    #     ],
    #   'Запеченный картофель': [
    #     {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    #     {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    #     {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    #     ]
    #   }
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

pprint(recipes(), width=100, sort_dicts = False)

def get_shp_l(dishes, person, recipe=recipes()):
    total = {}
    count = 0
   
    for dish in dishes:
        if dish in recipe:
            for iter in recipe[dish]:
                if iter['ingredient_name'] not in total:
                    # print(f"{iter['ingredient_name']}{int(iter['quantity'])*person} {iter['measure']}")
                    dd = {'quantity': int(iter['quantity'])*person, 'measure': iter['measure']}
                    total[iter['ingredient_name']] = dd
                else:
                    total[iter['ingredient_name']]['quantity'] += int(iter['quantity'])*person
    return total

pprint(get_shp_l(['Запеченный картофель','Омлет'], 2))