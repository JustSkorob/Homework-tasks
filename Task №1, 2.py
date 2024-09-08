import pprint


# Функция для чтения рецептов из файла и создания cook_book
def parse_cook_book(file_path):
    cook_book = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            dish_name = file.readline().strip()  # Название блюда
            if not dish_name:
                break  # Если строка пустая, заканчиваем обработку
            ingredients_count = int(file.readline().strip())  # Количество ингредиентов
            ingredients = []

            for _ in range(ingredients_count):
                ingredient_data = file.readline().strip().split(' | ')
                ingredient = {
                    'ingredient_name': ingredient_data[0],
                    'quantity': int(ingredient_data[1]),
                    'measure': ingredient_data[2]
                }
                ingredients.append(ingredient)

            cook_book[dish_name] = ingredients
            file.readline()  # Пропускаем пустую строку после списка ингредиентов

    return cook_book


# Функция для составления списка покупок по блюдам и количеству персон
def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}

    for dish in dishes:
        if dish in cook_book:  # Проверяем, что блюдо есть в книге рецептов
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count  # Умножаем количество на число персон
                measure = ingredient['measure']

                if ingredient_name in shop_list:
                    shop_list[ingredient_name]['quantity'] += quantity
                else:
                    shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}

    return shop_list


# Пример использования
file_name = 'Recipes.txt'
cook_book_list = parse_cook_book(file_name)

# Вызов функции для получения списка покупок
list_for_shop = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2, cook_book_list)

# Вывод результатов
print('Задание №1:')
pprint.pp(cook_book_list)
print('\n Задание №2:')
pprint.pp(list_for_shop)
