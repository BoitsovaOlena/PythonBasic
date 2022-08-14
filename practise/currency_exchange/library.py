from decimal import Decimal
from decimal import ROUND_HALF_EVEN


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
    if my_list[0] == 'EXCHANGE':
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
    if my_list[0] == 'STOP':
        if len(my_list) != 1:
            return None
        else:
            return {'command': my_list[0]}
    if my_list[0] == 'HELP':
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


class Currency:
    name = None
    _balance = None
    exchange_rate = None

    @property
    def balance(self) -> Decimal | None:
        return self._balance

    @balance.setter
    def balance(self, value: Decimal):
        if not isinstance(value, Decimal):
            raise TypeError
        self._balance = value

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
        return to_decimal(rate_item['rate']*val) if rate_item['flag'] == '+' else to_decimal(val/rate_item['rate'])
