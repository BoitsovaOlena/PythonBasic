from datetime import datetime


def function_runtime_find(func):
    """
    The function is a decorator. Defines the running time of the decorated function.

    :param func: Function for decorating.
    :param func: function
    :return: Function execution time in seconds.
    :rtype: str
    """
    def wrapper(*args, **kwargs):
        start = datetime.now()
        res = func(*args, **kwargs)
        end = datetime.now()
        print(f'Час гри в секундах: {(end - start).seconds}')
        return res
    return wrapper
