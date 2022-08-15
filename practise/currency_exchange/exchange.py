'''

Обмінник USD-UAH (система обліку валюти для касира)

Реалізувати функціонал обмінника USD и UAH валют за допомогою Python.

User Story: Після запуску файла користувач віддає команду:

     - отримання курсу валюти і залишків

        COURSE [CURRENCY NAME] - система перевіряє доступність валюти, ЇЇ курс и залишок


        COMMAND?
        >>> COURSE USD
        RATE 27.5, AVAILABLE 13500.98

        COMMAND?
        >>> COURSE UAH
        RATE 27.3, AVAILABLE 39345.5

        COMMAND?
        >>> COURSE BCH
        INVALID CURRENCY BCH

     - обмін

        EXCHANGE UAH 100 - система перевіряє чи доступна необхідна кількість USD в у відповідності до курсу, якщо кількість доступна - проводить обмфн і оновлює баланси

        COMMAND?
        >>> EXCHANGE UAH 100
        USD 3.6363, RATE 0.036363

        EXCHANGE USD 100 - система перевіряє чи доступна необхідна кількість UAH в у відповідності до курсу, якщо кількість доступна - проводить обмфн і оновлює баланси

        COMMAND?
        >>> EXCHANGE USD 100
        UAH 2730, RATE 27.3

        - якщо баланса валюти недостатньо
        COMMAND?
        >>> EXCHANGE USD 2000
        UNAVAILABLE, REQUIRED BALANCE UAH 54600, AVAILABLE 39345.5

     - зупинка сервісу
        STOP - програма завершується

        COMMAND?
        >>> STOP
        SERVICE STOPPED

Tech Requirements:
    Ввід данних за допомогою функції input.
    Стан системи (курс і доступний баланс валют для кожної валюти) зберігається в окремому файлі, формат файлу та даних в ньому визначається розробником.
    У випадку невірного вводу (невірне формат команди, невалідні дані) система має видати інформативне повідомлення,
    яке дасть оператору змогу зрозуміти в чому полягає помилка
    Важливо! Система має використовувати різний курс для кожного напрямку обміну. Наприклад USD->UAH курс 27.3, UAH->USD курс 27.9.

Additional:
    Опціонально як можливість для майбутнього розширення функціональності системи передбачити архітектурні можливості для додавання інших валют і виконання операцій з ними.

'''

# from pprint import pprint

from library import currency_transactions

messages = {
    'input_msg': '\033[0;34mCOMMAND?\n(Don\'t know what to do? Enter command: HELP)\n>>> \033[0m',
    'error_command': '\033[0;31mIncorrect command.\nThe program contains commands: HELP, STOP, COURSE, EXCHANGE.\n'
                     'Enter HELP to learn more\033[0m',
    'error_command_form': '\033[0;31mIncorrect command format.\nEnter HELP to learn more\033[0m',
    'error_currency': '\033[0;31mInvalid currency {}\033[0m',
    'course_msg': 'RATE {rate} {rate_to_currency} AVAILABLE {balance} {currency}',
    'exchange_msg': '{currency} {c_sum}, RATE {rate}',
    'error_exchange': '\033[0;31mUNAVAILABLE, REQUIRED BALANCE {currency} {c_sum}, AVAILABLE {available_amount}\033[0m',
    'error_currency_exchange': '\033[0;31mInvalid currency to which we exchange {}\033[0m',
    'help': 'The program contains commands: HELP, STOP, COURSE, EXCHANGE.\n'
            'Commands should be entered in capital letters.\n'
            '\033[0;33mTo find out how a certain command works, enter: HELP "command name"\033[0m\n'
            '\033[0;33mFor example: HELP COURSE\033[0m',
    'help_stop': 'The command stops the program.',
    'help_course': 'The command allows you to get the currency exchange rate\n'
                   '(relative to another specified currency) and its balance.\n'
                   'Commands should be entered in capital letters.\n'
                   '\033[0;33mFormat of the command: COURSE "currency" "currency to which we exchange"\033[0m\n'
                   'Currency names must be entered in alpha-3 format\n'
                   '\033[0;33mExample: COURSE USD UAH \033[0m',
    'help_exchange': 'Currency exchange command. If the operation is successful, the currency balances are updated,\n'
                     'and information about the bought currency and the exchange rate is displayed on the screen.\n'
                     'If there is not enough currency for exchange, the transaction is not carried out.'
                     'Commands should be entered in capital letters.\n'
                     '\033[0;33mFormat of the command: EXCHANGE "currency" "value to exchange" "currency to which we exchange"\033[0m\n'
                     'Currency names must be entered in alpha-3 format. Value must be int.\n'
                     '\033[0;33mExample: EXCHANGE USD 100 UAH \033[0m',
    'stop': 'SERVICE STOPPED'
}

currency_transactions(messages)
