from library import to_decimal

currencies = {
    "USD": {
        'balance': to_decimal('13500.98'),
        'exchange_rate': {
            "UAH": {
                'rate': to_decimal('27.3'),
                'flag': '+'
            }
        }
    },
    "UAH": {
        'balance': to_decimal('39345.5'),
        'exchange_rate': {
            "USD": {
                'rate': to_decimal('27.9'),
                'flag': '-'
            }
        }
    }

}
