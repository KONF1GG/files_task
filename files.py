from pprint import pprint

file = 'resepies.txt'

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

pprint(creat_cookbook(file), sort_dicts=False)


