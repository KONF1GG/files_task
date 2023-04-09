from pprint import pprint

file = 'resepies.txt'
people = 3

def creat_cookbook(file):
    with open(file, encoding='utf-8') as f:
        cookbook = {}
        for line in f:
            dish_name = line.strip()
            products_count = int(f.readline().strip())
            ingredients = []
            for _ in range(products_count):
                ingredient_name, quantity, measure = f.readline().strip().split(' | ')
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': quantity,
                    'measure': measure
                })
            f.readline()
            cookbook[dish_name] = ingredients

        return cookbook

def get_shop_list_by_dishes(dishes, person_count):
    cookbook = creat_cookbook(file)
    shop_list = {}
    for dish in dishes:
        ingredients = cookbook[dish]
        for ingredient in ingredients:
            ingredient_name, measure, quantity = ingredient['ingredient_name'],\
                ingredient['measure'], int(ingredient['quantity']) * person_count
            if ingredient_name in shop_list:
                shop_list[ingredient_name]['quantity'] += quantity
            else:
                shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}
    return shop_list

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Фахитос'], 2), sort_dicts=False)
