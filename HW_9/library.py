from random import randint
from decorator import function_runtime_find


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
        'start': '\033[0;30;43m"Вгадай число"\033[0m',
        'try': '\nКількість спроб - {}',
        'add_number': '\033[0;34mВведіть ваше число: \033[0m',
        'cold': 'Холодно!',
        'warm': 'Тепло!',
        'hot': 'Гаряче!',
        'win': '\033[0;30;43mВи перемогли!\033[0m',
        'game_over': '\033[0;30;43mГру закiнчено.\033[0m\n',
        'input_error': '\033[0;31mВи ввели некорректні дані. Потрібно ввести число від 1 до 100.\033[0m',
        'value_error': '\033[0;31mValueError: {}\033[0m'
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


def get_random_number(start=1, stop=100):
    """
    Returns a random number in the given interval. If no interval is specified, a number from 1 to 100 is taken.

    :param start: First number.
    :type start: int
    :param stop: Last number.
    :type stop: int
    :return: Random number in the given interval.
    :rtype: int
    """
    number = randint(start, stop)
    return number


def get_number_from_user():
    """
    Gets a number from the user. If the data entered by the user is not correct -
    displays an error message and makes a new request.

    :return: The number entered by the user, if it is valid.
    :rtype: int
    """
    while True:
        try:
            number = int(input(add_message('add_number')).strip(' '))
            if 0 < number <= 100:
                return number
            else:
                print(add_message('input_error'))
        except ValueError as error:
            print(add_message('value_error').format(error))


def check_numbers(to_guess, user_number):
    """
    The function checks the identity of the number to be guessed and the number entered by the user.
    If they are the same, returns True, otherwise - False.
    :param to_guess: A number that the user must guess.
    :type to_guess: int
    :param user_number: Number entered by the user.
    :type user_number: int
    :return:
    :rtype: bool
    """
    print(f'---> {to_guess}')
    if to_guess == user_number:
        return True
    else:
        differ = abs(to_guess - user_number)
        print(add_message('cold') if differ > 10 else add_message('warm') if 5 <= differ <= 10 else add_message('hot'))
        return False


@function_runtime_find
def game(attempts):
    """
    The purpose of the game is to guess the number chosen by the computer. The user has a limited number of attempts.
    If the difference between the user's number and the number to guess is more than 10, displays "Cold",
    if 5-10 - "Warm", if 1-4 "Hot".
    To win, the user must guess the number for a given amount of tries.

    :param attempts: The number of attempts the user has to guess the number.
    :type attempts: int
    :return:
    :rtype: None
    """
    if not isinstance(attempts, int):
        raise TypeError("The function 'game' expects to receive as an argument only int")
    print(add_message('start')+add_message('try').format(attempts))
    number_to_guess = get_random_number()
    counter = 0

    while attempts > counter:
        user_number = get_number_from_user()
        counter += 1
        if check_numbers(number_to_guess, user_number):
            print(add_message('win'))
            break

    print(add_message('game_over'))
