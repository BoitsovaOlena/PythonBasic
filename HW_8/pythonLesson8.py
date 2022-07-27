# Homework 8

# Напишіть гру "Камінь ножиці папір". Схема роботи така:
# -користувачу виводиться повідомлення зі списком фігур.
# -користувач обриає якусь фігуру, програма випадковим чином обирає свою.
# -визначається переможець
# Опціонально можна додати можливість запропонувати продовжувати гру (Y\N) і вести рахунок перемог.

from random import choice


def add_message(key, text_dict=None):
    """
    The function accepts 2 parameters: key and text_dict (dictionary) and returns the corresponding information message.
    Dictionary is not a required field, you can use the default value.

    :param key: The key corresponds to the message you are looking for.
    :type key: int|float|str|bool
    :param text_dict: Dictionary with a list of your messages. If not specified, the default dict 'messages' is used.
    :type text_dict:dict
    :return: Returns the message string. If an error occurred - an empty line.
    :rtype: str
    """
    messages = {
        'start': '\033[0;30;43m"Камінь ножиці папір"\033[0m',
        'choose_figure': '\033[0;34mВведіть ваш варіант (надрукуйте камінь, ножиці або папрір):\n\033[0m',
        'program_choose': 'Компьютер обрав {}',
        'win': 'Поздоровляю, ви виграли!',
        'loss': 'Упс, ви програли. Пощастить іншим разом.',
        'dead heat': 'У вас нічия',
        'score': '\033[0;34mРахунок: ви - {}, компьютер - {}.\033[0m',
        'continue_game': '\033[0;36mЧи бажаєте продавжити гру, введіть так або ні:\n\033[0m',
        'game_over': '\033[0;30;43mГру закiнчено.\033[0m\n',
        'input_error': 'Ви ввели некорректні дані. Такого варіанту в списку немає.',
        'type_error': '\033[0;31mTypeError: check_compliance() argument must be tuple\033[0m'
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


def check_compliance(items_list, request_message="Введіть ваш варіант: "):
    """
    The function is designed to check the presence of the entered value in the list. It takes the list as an argument.
    User enter his variant. If the user entered one of the values in the list, it is returned.
    If not, it displays an error message and offers to enter the data again.
    The second argument is a message for entering data, it has a default value "Введіть ваш варіант: ".

    :param items_list: List of valid values.
    :type items_list: tuple
    :param request_message: Message for entering data.
    :type request_message: str
    :return: Returns entered value or None.
    :rtype: str|None
    """
    if not isinstance(items_list, tuple):
        print(add_message('type_error'))
        return
    while True:
        item = input(request_message).strip(' ').lower()
        if item in items_list:
            return item
        else:
            print(add_message('input_error'))


def game():
    """
    Game "Rock, scissors, paper". The player enters his version of the figure through the console.
    The computer randomly chooses its figure. According to the result of the game, a message is issued about a loss,
    a win or a draw. After the end of the game, the player is asked to play again or to quit. He can play many games.
    If the player chooses to finish - a score is displayed in the console.

    :return:
    :rtype: None
    """
    figures = ('камінь', 'ножиці', 'папір')
    score = {
        'player': 0,
        'computer': 0
    }
    print(add_message('start'))
    while True:
        player_figure = check_compliance(items_list=figures, request_message=add_message('choose_figure'))
        computer_figure = choice(figures)
        print(add_message('program_choose').format(computer_figure))
        win_condition_1 = player_figure == 'камінь' and computer_figure == 'ножиці'
        win_condition_2 = player_figure == 'ножиці' and computer_figure == 'папір'
        win_condition_3 = player_figure == 'папір' and computer_figure == 'камінь'
        if player_figure == computer_figure:
            print(add_message('dead heat'))
        elif win_condition_1 or win_condition_2 or win_condition_3:
            score['player'] += 1
            print(add_message('win'))
        else:
            score['computer'] += 1
            print(add_message('loss'))
        want_continue = check_compliance(items_list=('так', 'ні'), request_message=add_message('continue_game'))
        if want_continue == 'ні' or not want_continue:
            print(add_message('game_over') + add_message('score').format(score['player'], score['computer']))
            return


game()
