# Homework 5

# Task 1:
# завантажити використовуючи requests структуру даних з
# https://dummyjson.com/todos
# та вивести на екран не виконані значення  з тих даних, які до вас прийшли

import requests
from pprint import pprint

url = 'https://dummyjson.com/todos'
todos_raw = requests.get(url)
todos = todos_raw.json()

print('\n********************\n')
print('Отримана структура данних')
pprint(todos)

todos_ot_completed = [
    todos['todos'][i]['todo'] for i in range(todos['limit']) if todos['todos'][i]['completed'] is False
]
print('\n********************\n')
print('Список не виконанних завдань')
pprint(todos_ot_completed)

# Якщо є необхідність більш детального аналізу з відстажанням можливої відсутності ключа 'completed'
# ожна використати наступний спосіб. Але мені здається що він ускладнює задачу і така помилка не має
# виникати при роботі з усталеними даними.

# todos_ot_completed = []
# for item in todos['todos']:
#     try:
#         if item['completed'] == False:
#             todos_ot_completed.append(item['todo'])
#     except KeyError as error:
#         todos_ot_completed = []
#         print(f'На жаль сталася помилка {error} і ми не можемо вивести список усіх не виконанних завдань.')
#         break
# if len(todos_ot_completed) > 0:
#     pprint(todos_ot_completed)
