from pprint import pprint

file_name = "recipes.txt"


def catalog_reader(file_name: str) -> dict:
    with open(file_name) as file:
        cook_book = {}
        for line in file:
            dish_name = line.strip()
            cook_book[dish_name] = []
            ingredients = []
            ingredient_count = file.readline()
            for item in range(int(ingredient_count)):
                ingredient = file.readline().replace('\n', '')
                ingredient_list = ingredient.split(sep='|')
                key_list = ['ingredient_name', 'quantity', 'mesure']
                ingredient_dict = dict(zip(key_list, ingredient_list))
                ingredients.append(ingredient.strip())
                cook_book[dish_name].append(ingredient_dict)

            file.readline()
        return cook_book


menu_dict = catalog_reader(file_name)


def get_shop_list_by_dishes(dishes, person_count):
    cook_dict = {}

    for dish in dishes:
        if dish in menu_dict.keys():

            for ingredients in menu_dict[dish]:
                quantity = int(ingredients['quantity']) * person_count
                if ingredients['ingredient_name'] in cook_dict.keys():
                    cook_dict[ingredients['ingredient_name']]['quantity'] += quantity
                else:
                    cook_dict[ingredients['ingredient_name']] = {'quantity': quantity, 'measure': ingredients['mesure']}
        else:
            print(f'{dish} блюда нет в списке')
    return cook_dict


pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))
