# Homework 9

# Візьміть гру з заняття і доопрацюйте її наступним чином:
# -всі функції в окремий файл
# -додайте підказки при вгадуванні (якщо різниця між числом користувача і загаданим більше 10 - вивести "Холодно",
#  якщо 5-10 - "Тепло", якщо 1-4 "Гаряче")
# -додайте можливість на початку програми вказати кількість спроб вгадування. користувач має вгадати число за вказану
#  кількість спроб
# Напишіть декоратор, який вимірює і виводить на екран час виконання функції в секундах і задекоруйте ним
# основну функцію гри. Після закінчення гри декоратор має сповістити, скільки тривала гра.

from library import game

game(attempts=3)
