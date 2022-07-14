# Homework 4

# Task 3:
# Є дані студентів (комбінація імені та прізвища унікальна), що зберігаються за допомогою словника
# 1 - програмно добавити одного студента, з заповненням усіх полів (вік - від 18 до 40, цілочисельне значення,
#     бал від 0 до 100 (інт чи флоат)
# 2 - створити і вивести на екран список студентів (імя та прізвище та середній бал), у яких середній бал більше 90
#     сам формат наповнення цього списку up to you
# 3 - визначити середній бал по групі
# 4 - при відсутності номеру телефону у студента записати номер деканату як значення за замовчуванням
# (номер на ваш вибір)
from pprint import pprint
students = {
    'Іван Петров': {
        'Пошта': 'Ivan@gmail.com',
        'Вік': 21,
        'Номер телефону': '+380987771221',
        'Середній бал': 95.8
    },
    'Женя Курич': {
        'Пошта': 'Geka@gmail.com',
        'Вік': 22,
        'Номер телефону': None,
        'Середній бал': 64.5
    },
    'Маша Кера': {
        'Пошта': 'Masha@gmail.com',
        'Вік': 18,
        'Номер телефону': '+380986671221',
        'Середній бал': 80
    },
}
messages = {
    'add_name': 'Вкажіть імя студента (допустимі тільни літери): ',
    'add_surname': 'Вкажіть прізвище студента (допустимі тільни літери): ',
    'add_email': 'Вкажіть email студента: ',
    'add_age': 'Вкажіть вік студента: ',
    'add_phone': 'Вкажіть номер телефону студента: +380',
    'add_GPA': 'Вкажіть середній бал студента: ',
    'wrong_email': 'Email вказано не вірно. Портібний формат: jnbdbn@jvdnj.hbvh або пусте поле',
    'wrong_age': 'Вік вказано не вірно. Вік - від 18 до 40, цілочисельне значення',
    'wrong_phone': 'Телефон вказано не вірно. Номер телефону маэ складатись з 9 цифр або бути пусти полем',
    'wrong_GPA': 'Середній бал вказано не вірно. Він має бути від 0 до 100',
    'excellent_list': 'Список відмінників:',
    'no_excellent': 'У списку студентів немає жодного відмінника.',
    'list': '\nСписок студентів'
}

# Отримуємо дані для заповнення нового студента.
# Виходимо з того що ми даємо користувачу ввести необхідні дані.
# Оскільки розявнень не було, я роблю перевірку на кожне з введених значенью
# Якщо введено некорректні дані запит повторюється.

new_student = {
    'name': None,
    'surname': None,
    'email': None,
    'age': None,
    'phone': None,
    'GPA': None
}
while True:
    new_student['name'] = input(messages['add_name']).strip(' ')
    if new_student['name'].isalpha():
        break
while True:
    new_student['surname'] = input(messages['add_surname']).strip(' ')
    if new_student['surname'].isalpha():
        break
while True:
    new_student['email'] = input(messages['add_email']).strip(' ')
    if new_student['email'].count('@') == 1 and new_student['email'].count('.') > 0:
        break
    elif new_student['email'] == '':
        new_student['email'] = None
        break
    else:
        print(messages['wrong_email'])
while True:
    try:
        new_student['age'] = int(input(messages['add_age']).strip(' '))
        if 17 < new_student['age'] < 41:
            break
        else:
            print(messages['wrong_age'])
    except ValueError as error:
        print(error)
while True:
    phone = input(messages['add_phone']).strip(' ')
    if phone.isdigit() and len(phone) == 9:
        new_student['phone'] = '+380' + phone
        break
    elif phone == '':
        break
    else:
        print(messages['wrong_phone'])
while True:
    gpa = input(messages['add_GPA']).strip(' ')
    if gpa.count('.') == 1:
        try:
            new_student['GPA'] = float(gpa)
            if 0 < new_student['GPA'] < 100:
                break
        except ValueError as error:
            print(error)
    elif gpa.isdigit():
        try:
            new_student['GPA'] = int(gpa)
            if 0 < new_student['GPA'] < 100:
                break
            else:
                print(messages['wrong_GPA'])
        except ValueError as error:
            print(error)
    else:
        print(messages['wrong_GPA'])

# Додаэмо нового студента в нашу коллекцію

new_key = new_student['name'].lower().title() + " " + new_student['surname'].lower().title()
students[new_key] = {
        'Пошта': new_student['email'],
        'Вік': new_student['age'],
        'Номер телефону': new_student['phone'],
        'Середній бал': new_student['GPA']
    }
print(messages['list'])
pprint(students)

# Cписок студентів (імя та прізвище та середній бал), у яких середній бал більше 90

excellent_students = set()
for key, value in students.items():
    if value.get('Середній бал') and value.get('Середній бал') > 90:
        excellent_students.add(f'{key} - {value.get("Середній бал")}')
if len(excellent_students) > 0:
    print('********************\n', messages['excellent_list'])
    for item in excellent_students:
        print(item)
else:
    print('********************\n', messages['no_excellent'])
print('********************\n')

# Визначаємо середній бал по групі

total_gpa = 0
unknown_gpa = 0
for value in students.values():
    if value.get('Середній бал'):
        total_gpa +=value.get('Середній бал')
    else:
        unknown_gpa += 1
medium_gpa = total_gpa/(len(students) - unknown_gpa)
print('Cередній бал по групі - ', medium_gpa)

# При відсутності номеру телефону записати номер деканату як значення за замовчуванням

dec_number = '+380501234567'
for value in students.values():
    try:
        if value['Номер телефону'] == None:
            value['Номер телефону'] = dec_number
    except:
        value['Номер телефону'] = dec_number
print(messages['list'] + ' з доданими номерами телефонів')
pprint(students)
