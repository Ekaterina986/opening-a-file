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
                ingredient = file.readline()
                ingredient_list = ingredient.split(sep='|')
                key_list = ['ingredient_name', 'quantity', 'mesure']
                ingredient_dict = dict(zip(key_list, ingredient_list))
                ingredients.append(ingredient.strip())
                cook_book[dish_name].append(ingredient_dict)

            file.readline()
        return cook_book


menu = catalog_reader(file_name)
pprint(menu)
