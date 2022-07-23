# Homework 7

# Знову апишіть программу "Касир в кінотеатрі", яка буде виконувати наступне:
# Попросіть користувача ввести свсвій вік.
# - якщо користувачу менше 7 - вивести "Тобі ж <>! Де твої батьки?"
# - якщо користувачу менше 16 - вивести "Тобі лише <>, а це е фільм для дорослих!"
# - якщо користувачу більше 65 - вивести "Вам <>? Покажіть пенсійне посвідчення!"
# - якщо вік користувача складається з однакових цифр (11, 22, 44 і тд років, всі можливі варіанти!) - вивести "О, вам <>! Який цікавий вік!"
# - у будь-якому іншому випадку - вивести "Незважаючи на те, що вам <>, білетів всеодно нема!"
# Замість <> в кожну відповідь підставте значення віку (цифру) та правильну форму слова рік
# Для будь-якої відповіді форма слова "рік" має відповідати значенню віку користувача.
# Наприклад :
# "Тобі ж 5 років! Де твої батьки?"
# "Вам 81 рік? Покажіть пенсійне посвідчення!"
# "О, вам 33 роки! Який цікавий вік!"

def add_message(key, text_dict=None):
    """
    Функція приймає 2 параметри: key (ключ) і text_dict(словник) та повертає відповідне інформаційне повідомлення.
    Словник не є обовязковим полем, можна використовувати дефолтне значення.

    :param key: Ключ відповідний шуканому повідомленню.
    :type key: int|float|str|bool
    :param text_dict: Словник з переліком ваших повідомлень. Якщо не вказано, використовується дефолтний dict messages.
    :type text_dict:dict
    :return: Певертає стрічку-повідомлення. Якщо сталася помилка - пусту стрічку.
    :rtype: str
    """
    messages = {
        'add_age': 'Будь ласка, вкажіть свій вік:\n',
        'age_error': 'Помилка! Допустимий вік від 1 до 200 років.\nЛише цілі числа.',
        'client_under_7': 'Тобі ж {}! Де твої батьки?',
        'client_under_16': 'Тобі лише {}, а це е фільм для дорослих!',
        'client_over_65': 'Вам {}? Покажіть пенсійне посвідчення!',
        'interesting_age': 'О, вам {}! Який цікавий вік',
        'no_tickets': 'Незважаючи на те, що вам {}, білетів всеодно нема!'
    }
    text_dict = messages if text_dict is None else text_dict
    try:
        return text_dict[key]
    except KeyError as error:
        print('Помилка! Ключа, який ви ввели не існує: ', error)
        return ''
    except TypeError as error:
        print('Помилка! Ви ввели дані невідповідного типу', error)
        return ''


def age_to_str(age):
    """
    Функція приймає числове значення віку та перетворює його на стрічку що містить число -
    вказаний вік та слово "рік" у відповідному відмінку.

    :param age: Вік, ціле число.
    :type age: int
    :return: Стрічка що містить число - вказаний вік та слово "рік" у відповідному відмінку.
    :rtype: str
    """
    str_age = str(age)
    ends_2 = str_age[-1] == '2' and str_age[-2:] != '12'
    ends_3 = str_age[-1] == '3' and str_age[-2:] != '13'
    ends_4 = str_age[-1] == '4' and str_age[-2:] != '14'
    if str_age[-1] == '1' and str_age[-2:] != '11':
        return f'{str_age} рік'
    elif ends_2 or ends_3 or ends_4:
        return f'{str_age} роки'
    else:
        return f'{str_age} років'


def get_age():
    """
    Функція запитує у користувача дані - вік користувача.
    У випадку введення некоректної інформації виподить відповідне повідомлення та знову запрошує дані.
    Допустимими є цілі числа більші за 1 і менші за 200.
    Якщо введено коректні дані - повертає введене число.

    :return: Повертає вік користувача.
    :rtype: int
    """
    max_age = 200
    while True:
        age = input(add_message('add_age')).strip(' ').lstrip('0')
        if age.isdigit() and int(age) < max_age:
            return int(age)
        else:
            print(add_message('age_error'))


def print_message(client_age):
    """
    Функція приймає вік клієнта, та повертає відповідне цьому віку текстове повідомлення.

    :param client_age: Вік користувача.
    :type client_age: int
    :return: Інформаційне повідомлення, відповідне віку користувача.
    :rtype: str
    """
    if not client_age:
        return
    elif client_age < 7:
        print(add_message('client_under_7').format(age_to_str(age=client_age)))
    elif str(client_age).count(str(client_age)[0]) == len(str(client_age)) and len(str(client_age)) > 1:
        print(add_message('interesting_age').format(age_to_str(age=client_age)))
    elif client_age < 16:
        print(add_message('client_under_16').format(age_to_str(age=client_age)))
    elif client_age > 65:
        print(add_message('client_over_65').format(age_to_str(age=client_age)))
    else:
        print(add_message('no_tickets').format(age_to_str(age=client_age)))


print_message(client_age=get_age())
