import datetime
import functools

"критерієм перевірки буде проходження всіх ассертів"

##############################################################################
############                                                     #############
############                      TASK 1                         #############
############                                                     #############
##############################################################################
"""
написати декоратор wrap_validate, який не приймає жодних параметрів
його задача - перевірити, що функція, яку він задекорував, обовязково отримала
в своїх аргументах параметр 'password' (згадуємо про * в написанні аргументів функції)
значення 'password' повинне бути стрічкою, довжиною не менше 10 символів,
та містити в собі латинські літери (регістр не принципово), арабські цифри та знак '!"

кожну з перевірок отриманого значення паролю виконуємо в ОКРЕМІЙ функції, функції робимо
універсальними, називаємо їх (з опційними параметрами)
- is_valid_length(length=10)
- has_any_symbols(symbols='qwertyuiopasdfghjklzxcvbnm') (це приклад для латинських букв, повертає тру, якщо хоч
один символ в стрічці, аналогічно зробити для цифр та знаку оклику (у вас буде 3 виклики функції в середині декоратора
з різними параметрами)
- is_string()

якщо  'password'  відсутній - викликаємо помилку
raise AttributeError(f'no parameter "password" in arguments of function{func.__name__}')

якщо  'password'  не задовольняє вимогам валідації, написаним вище, то повертається словник виду
{ 'result': str(func(*args, **kwargs)),
  'is_secure': False,
}

якщо  'password'  задовольняє вимогам валідації, написаним вище, то повертається словник виду
{ 'result': str(func(*args, **kwargs)),
  'is_secure': True,
}

зауважте, що str(func(*args, **kwargs)) МАЄ бути довжиною не більше 100 символів
якщо даний результат буде довшим за 100 символів, то стрічка має бути обрізана до 100 символів, причому останні
три символи мають бути ... (трьома крапками)
тут ви вже й самы здогадалися написати функцію на виконання даної роботи (тут вже без підказок)
"""


def is_string(item) -> bool:
    return True if isinstance(item, str) else False


def is_valid_length(my_str: str, length: int) -> bool:
    return True if len(my_str) >= length else False


def has_any_symbols(my_str, symbols):
    """
    The function checks the presence of characters from the second string in the first string.
    :param my_str: String for verification.
    :type my_str: str
    :param symbols: List of symbols.
    :type symbols: str
    :return: Returns True if at least one match is found. Otherwise False.
    :rtype: bool
    """
    chack_str = my_str.lower()

    set_symbols = set(symbols)
    for symbol in set_symbols:
        if chack_str.count(symbol):
            return True
    return False


def cut_string(my_str: str, length: int) -> str:
    return my_str if len(my_str) <= length else my_str[0:(length-3)]+'...'


def wrap_validate(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        password = kwargs.get('password')
        if password is None:
            raise AttributeError(f'no parameter "password" in arguments of function {func.__name__}')
        result = cut_string(str(func(*args, **kwargs)), 100)
        res = {'result': result,
                'is_secure': False
               }
        if not is_string(password):
            return res
        if not is_valid_length(my_str=password, length=10):
            return res
        if not has_any_symbols(my_str=password, symbols='qwertyuiopasdfghjklzxcvbnm'):
            return res
        if not has_any_symbols(my_str=password, symbols='1234567890'):
            return res
        if not has_any_symbols(my_str=password, symbols='!'):
            return res
        res['is_secure'] = True
        return res
    return wrapper


##############################################################################
############                                                     #############
############                      TASK 2                         #############
############                                                     #############
##############################################################################
"""
написати функцію registration, яка приймає
- позиційний аргумент id, стрічка або число - не важливо,  значення за замовчуванням - відсутнє
- позиційний або іменований аргумент login, тип даних - не важливий, значення за замовчуванням - відсутнє
- позиційний або іменований аргумент notes, тип даних - не важливий, значення за замовчуванням - відсутнє
- password - тип даних - не важливий, значення за замовчуванням - відсутнє

в середині функції вставити код (зназок для отримання даних прописаний нижче)
date = datetime.date.today()

результат робити функції - стрічка
f'User {login} created account on {date} with password "{password}". Additional information: {notes}'

задекоруйте написаним в завданні 1 декоратором
"""

# Опис функції зроблено з урахуванням декоратора. Не знаю як правильно надати інформацію, враховуючи те що
# декоратор змінює вигляд даних, що повертаються.
@wrap_validate
def registration(id, /, login, notes, *, password):
    """
    The function receives user data and returns a dict with informational message about creating an account and
    about password validation.
    :param id: ID of user.
    :type id: int|str
    :param login: User login.
    :param notes: Some notes.
    :param password: User password.
    :return: Information about created account and about password validation.
    :rtype: dict
    """
    date = datetime.date.today()
    return f'User {login} created account on {date} with password "{password}". Additional information: {notes}'

print(registration(1, 'gkjnk', 'jhbjkj', password="sknsanvlsakn56!"))



##############################################################################
############                                                     #############
############                      TASK 3                         #############
############                                                     #############
##############################################################################
"""
створіть умову if name == main (тут ціленаправлено написано не вірно, як вірно - ви знаєте)
в цій умові створіть assert на всі створені функції (окрім декоратора), викликайте функції з різними параметрами 
(довжина слів, різні текстовки....)
на кожну функцію, що використовується в декораторі, має бути мінімум 3 ассерта,

функцію registration перевіряйте з огляду на роботу декоратора (ключі, значення). обовязково перевірте кількість ключів, 
тип даних в значеннях, назви ключів, значення отриманого результату в залежності від переданих даних   

ВАЖЛИВО 
функцію registration ассертимо ТІЛЬКИ при передачі їй валідних даних (поля паролю)
"""

if __name__ == '__main__':
    assert is_string(5) is False, 'It\'s not a string. False value "True"'
    assert is_string('bkjnlkn') is True, 'It\'s a string. False value "False"'
    assert type(is_string('bkjnlkn')) is bool, 'Not a bool'
    assert is_valid_length(my_str='123', length=10) is False, 'It\'s not long enough. False value "True"'
    assert is_valid_length(my_str='dfsgjj', length=3) is True, 'It\'s long enough. False value "False"'
    assert type(is_valid_length(my_str='sadkjad', length=10)) is bool, 'Not a bool'
    assert has_any_symbols(my_str='', symbols='134') is False, \
        'There are no such symbols in the string. False value "True"'
    assert has_any_symbols(my_str='dsvfdkj85435', symbols='sfewsfn egmg') is True, \
        'There are such symbols in the string. False value "False"'
    assert type(has_any_symbols(my_str='scC sdv', symbols='swww1')) is bool, 'Not a bool'
    assert len(cut_string(my_str='adc', length=10)) == 3, 'Incorrect string length'
    assert len(cut_string(my_str='adcekfpoekfpoek', length=5)) == 5, 'Incorrect string length'
    assert cut_string(my_str='adcekfpoekfpoek', length=5) == 'ad...', 'Incorrect result'
    assert type(cut_string(my_str='adcekfpoekfpoek', length=5)) is str, 'Not a str'
    assert registration(1, 'Djon', '', password="sknsanvlsakn56!")['is_secure'] is True, 'It\'s secure. False value "False"'
    assert registration(1, 'Djon', '', password="0123!JKGFHJJHF")['is_secure'] is True, 'It\'s secure. False value "False"'
    assert type(registration(1, 'Sem', '', password="sknsanvlsakn56!")) == dict, 'not a dict'



##############################################################################
############                                                     #############
############                      TASK 4                         #############
############                     HAVE FUN                        #############
############                                                     #############
##############################################################################

file = open('example.txt', 'w')

file.write(registration(1, 'Djon', '', password="123win321WIN!")['result'])

file.close()
