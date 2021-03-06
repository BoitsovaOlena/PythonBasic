# Homework 2

# Напишіть программу "Касир в кінотеватрі", яка буде виконувати наступне:
# Попросіть користувача ввести свсвій вік (можно використати константу або функцію input()).
# - якщо користувачу менше 7 - вивести "Де твої батьки?"
# - якщо користувачу менше 16 - вивести "Це фільм для дорослих!"
# - якщо користувачу більше 65 - вивести "Покажіть пенсійне посвідчення!"
# - якщо вік користувача складається з однакових цифр (11, 22, 44 і тд років, всі можливі варіанти!)
# - вивести "Який цікавий вік!"
# - у будь-якому іншому випадку - вивести "А білетів вже немає!"

age = input('Будь ласка, вкажіть свій вік:\n').strip(' ')
# При виконанні завдання виходжу з того що після введення віку виводиться лише 1 повідомлення
if age.isdigit():
    int_age = int(age)
    if int_age == 0:
        print('А білетів вже немає!')
        # При виконанні завдання виходжу з того, що у випалку введення помилкових даних
        # також виводимо 'А білетів вже немає!'.
        # Інакше в цьому пункті можна вивести попрередження типу "Некоректний формат даних"
    elif int_age < 7:
        print('Де твої батьки?')
    elif (len(age) == 2 and age[0] == age[1]) or int_age == 111:
        print('Який цікавий вік!')
    elif int_age < 16:  # Вік починається з одного року
        print('Це фільм для дорослих!')
    elif int_age > 200:  # Обмеження віку до 200 років
        print('А білетів вже немає!')
        # При виконанні завдання виходжу з того, що у випалку введення помилкових даних
        # також виводимо 'А білетів вже немає!'.
        # Інакше в цьому пункті можна вивести попрередження типу "Некоректний формат даних"
    elif int_age > 65:
        print('Покажіть пенсійне посвідчення!')
    else:
        print('А білетів вже немає!')
else:
    print('А білетів вже немає!')
    # При виконанні завдання виходжу з того, що у випалку введення помилкових даних
    # також виводимо 'А білетів вже немає!'.
    # Інакше в цьому пункті можна вивести попрередження типу "Некоректний формат даних"
