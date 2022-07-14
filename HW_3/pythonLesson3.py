# Homework 3

# Task 1:
# Зформуйте строку, яка містить певну інформацію про символ в відомому слові.
# Наприклад "The [номер символу] symbol in [тут слово] is '[символ з відповідним порядковим номером]'".
# Слово та номер отримайте за допомогою input() або скористайтеся константою.
# Наприклад (слово - "Python" а номер символу 3) - "The 3 symbol in "Python" is 't' ".

while True:
    word = input('Будь ласка, введіть слово: ').strip(' ')
    symbol_number = input('Будь ласка, вкажіть номер символу: ').strip(' ')
    if word.isalpha() and symbol_number.isdigit():
        int_index = int(symbol_number) - 1
        if int(symbol_number) == 0:
            print(
                'Ви ввели некорректні дані. Спробуйте ще! \n(Номер літери не може дорівнювати 0)')
            continue
        elif len(word) > int_index:
            result_string = f"Літера №{symbol_number} у слові '{word}' це {word[int_index]}"
            print('Відповідь:', result_string)
        else:
            print('Ви ввели некорректні дані. Спробуйте ще! \n(Номер символу більше довжини слова)')
            continue
        break
    print('Ви ввели некорректні дані. Спробуйте ще! \n(Cлово моє складатися з літер, а номер має бути цілим числом.)')

# Task 2:
# Вести з консолі строку зі слів за допомогою input() (або скoристайтеся константою).
# Напишіть код, який визначить кількість слів, в цих даних.

string = input('Будь ласка, введіть вашу строку: ').strip(' ')
if string.isdigit() or len(string) == 0:
    print("Некорректно введені дані")
else:
    words = string.split(' ')
    words_counter = 0
    for word in words:
        if len(word) > 0:
            words_counter += 1
    print(f"Кількість слів у цій строці -  {words_counter}")

# Task 3:
# Існує ліст з різними даними, наприклад
# lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який сфлрмує новий list (наприклад lst2),
# який би містив всі числові змінні (int, float), які є в lst1.
# Майте на увазі, що данні в lst1 не є статичними можуть змінюватись від запуску до запуску.

lst = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
numbers_lst = []
if len(lst) > 0:
    for item in lst:
        if str(type(item)) == "<class 'int'>" or str(type(item)) == "<class 'float'>":
            numbers_lst.append(item)
    if len(numbers_lst) > 0:
        print('Список чисел: ', numbers_lst)
    else:
        print('В вашому списку немає жодного числа.')
else:
    print('Початковий список пустий.')
