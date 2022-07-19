# Homework 6

# Task 1:
# Напишіть функцію, що приймає один аргумент будь-якого типу та повертає цей аргумент, перетворений на float.
# Якщо перетворити не вдається функція має повернути 0.

def convert_to_float(item):
    try:
        return float(item)
    except (ValueError, TypeError):
        return 0


print('Завдання 1.\nРезультат перетворення на float: ', convert_to_float(None))

# Task 2:
# Напишіть функцію, що приймає два аргументи. Функція повинна
# -якщо аргументи відносяться до числових типів (int, float) - повернути перемножене значення цих аргументів,
# -якщо обидва аргументи це строки - обʼєднати в одну строку та повернути
# -якщо перший строка, а другий ні - повернути dict де ключ це перший аргумент, а значення - другий
# -у будь-якому іншому випадку повернути кортеж з цих аргументів

# Варыант 1 - спрощений і підходить для таких нескладних завдань.


def data_processing(data_1, data_2):
    isnumber_data1 = type(data_1) == int or type(data_1) == float
    isnumber_data2 = type(data_2) == int or type(data_2) == float
    if isnumber_data1 and isnumber_data2:
        return data_1*data_2
    elif type(data_1) == str and type(data_2) == str:
        return data_1 + data_2
    elif type(data_1) == str and type(data_2) != str:
        return {data_1: data_2}
    else:
        return data_1, data_2


print('Завдання 2 (перший варіант).\nРезультат перетворення 2x аргументів: ', data_processing(6, 2))

# Варыант 2 - трохи складніший, проте правильніший з точки зору логіки створення програмного коду.
# Операції з розрахунків винесені з основної функції, яка перевіряє вхідні дані.


def multiplication(num_1, num_2):
    return num_1*num_2


def str_union(str_1, str_2):
    return str_1 + str_2


def create_dict(key, value):
    return {key: value}


def create_tuple(item_1, item_2):
    return item_1, item_2


def data_processing(data_1, data_2):
    isnumber_data1 = type(data_1) == int or type(data_1) == float
    isnumber_data2 = type(data_2) == int or type(data_2) == float
    if isnumber_data1 and isnumber_data2:
        return multiplication(num_1=data_1, num_2=data_2)
    elif type(data_1) == str and type(data_2) == str:
        return str_union(str_1=data_1, str_2=data_2)
    elif type(data_1) == str and type(data_2) != str:
        return create_dict(key=data_1, value=data_2)
    else:
        return create_tuple(item_1=data_1, item_2=data_2)


print('Завдання 2 (другий варіант).\nРезультат перетворення 2x аргументів: ', data_processing(5, "2"))
