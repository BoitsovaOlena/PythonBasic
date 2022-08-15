from decimal import Decimal
from decimal import ROUND_HALF_EVEN
import functools
import json


class Currency:
    name = None
    _balance = None
    exchange_rate = None

    @property
    def balance(self) -> Decimal | None:
        return self._balance

    @balance.setter
    def balance(self, value: str|Decimal):
        if not isinstance(value, str|Decimal):
            raise TypeError
        self._balance = to_decimal(value)

    def __init__(self, name: str, balance: Decimal, exchange_rate: dict):
        self.name = name
        self.balance = balance
        self.exchange_rate = exchange_rate

    @property
    def currency_dict(self):
        return {'name': self.name, 'balance': self.balance, 'exchange_rate': self.exchange_rate}

    def get_rate(self, currency_name):
        for key, val in self.exchange_rate.items():
            if currency_name == key:
                return val['rate'] if val['flag'] == '+' else f'1/{val["rate"]}'
        return None

    def exchange(self, item, val):
        rate_item = self.exchange_rate.get(item.name)
        if rate_item is None:
            return None
        return to_decimal(to_decimal(rate_item['rate'])*val) if rate_item['flag'] == '+' else to_decimal(val/to_decimal(rate_item['rate']))


def to_decimal(val):
    return Decimal(val).quantize(Decimal('0.01'), rounding=ROUND_HALF_EVEN)


def commands_to_dict(command):
    my_list = command.split()
    if my_list[0] == 'COURSE':
        if len(my_list) != 3:
            return None
        else:
            conditions = (
                len(my_list[1]) == 3,
                len(my_list[2]) == 3
            )
            return {
                'command': my_list[0],
                'currency': my_list[1],
                'rate_to': my_list[2]
            } if all(conditions) else None
    elif my_list[0] == 'EXCHANGE':
        if len(my_list) != 4:
            return None
        else:
            conditions = (
                len(my_list[1]) == 3,
                my_list[2].isdigit(),
                len(my_list[3]) == 3
            )
            return {
                'command': my_list[0],
                'currency': my_list[1],
                'exchange_val': my_list[2],
                'rate_to': my_list[3]
            } if all(conditions) else None
    elif my_list[0] == 'STOP':
        if len(my_list) != 1:
            return None
        else:
            return {'command': my_list[0]}
    elif my_list[0] == 'HELP':
        if len(my_list) > 2:
            return None
        elif len(my_list) == 1:
            return {
                'command': my_list[0],
                'command_to_help': None
            }
        else:
            conditions = (
                my_list[1] == 'STOP',
                my_list[1] == 'COURSE',
                my_list[1] == 'EXCHANGE'
            )
            return {
                'command': my_list[0],
                'command_to_help': my_list[1]
            } if any(conditions) else None
    else:
        return 'False command'


def get_currencies(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        with open('currencies.json', 'r') as file:
            currencies = json.loads(file.read())
        for key, val in currencies.items():
            globals()[f'{key}'] = Currency(key, val['balance'], val['exchange_rate'])
        res = func(*args, **kwargs)
        return res
    return wrapper


@get_currencies
def currency_transactions(messages):
    while True:
        command_string = input(messages['input_msg']).strip(' ').upper()
        command_dict = commands_to_dict(command_string)
        if command_dict == 'False command':
            print(messages['error_command'])
        elif command_dict is None:
            print(messages['error_command_form'])
        elif command_dict['command'] == 'COURSE':
            item = globals().get(f'{command_dict["currency"]}')
            if item:
                rate = item.get_rate(command_dict["rate_to"])
                if rate:
                    print(messages['course_msg'].format(
                        rate=rate,
                        rate_to_currency=command_dict["rate_to"],
                        balance=item.balance,
                        currency=item.name
                    ))
                else:
                    print(messages['error_currency_exchange'].format(command_dict["rate_to"]))
            else:
                print(messages['error_currency'].format(command_dict["currency"]))
        elif command_dict['command'] == 'EXCHANGE':
            item = globals().get(f'{command_dict["currency"]}')
            rate_to_item = globals().get(f'{command_dict["rate_to"]}')
            if not item:
                print(messages['error_currency'].format(command_dict["currency"]))
            elif not rate_to_item:
                print(messages['error_currency'].format(command_dict["rate_to"]))
            else:
                exchange_amount = to_decimal(command_dict["exchange_val"])
                amount_after_exchange = item.exchange(rate_to_item, exchange_amount)
                available_amount = rate_to_item.balance
                if amount_after_exchange is None:
                    print(messages['error_currency_exchange'].format(rate_to_item.name))
                elif available_amount >= amount_after_exchange:
                    print(messages['exchange_msg'].format(
                        currency=rate_to_item.name,
                        c_sum=amount_after_exchange,
                        rate=item.get_rate(rate_to_item.name)
                    ))
                    item.balance += exchange_amount
                    rate_to_item.balance -= amount_after_exchange
                else:
                    print(messages['error_exchange'].format(
                        currency=rate_to_item.name,
                        c_sum=amount_after_exchange,
                        available_amount=available_amount
                    ))
        elif command_dict['command'] == 'HELP':
            if command_dict['command_to_help'] is None:
                print(messages['help'])
            elif command_dict['command_to_help'] == 'EXCHANGE':
                print(messages['help_exchange'])
            elif command_dict['command_to_help'] == 'STOP':
                print(messages['help_stop'])
            elif command_dict['command_to_help'] == 'COURSE':
                print(messages['help_course'])

        elif command_dict['command'] == 'STOP':
            with open('currencies.json', 'r') as file:
                currencies_file = file.read()
                currencies_file = json.loads(currencies_file)
                for key, val in currencies_file.items():
                    item = globals().get(f'{key}')
                    if item:
                        currencies_file[key]['balance'] = str(item.balance)
            with open('currencies.json', 'w') as file:
                file.write(json.dumps(currencies_file))
            print(messages['stop'])
            break
