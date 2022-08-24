# Homework 16
"""
Підключіться до API НБУ ( документація тут https://bank.gov.ua/ua/open-data/api-dev ), отримайте курс валют і запишіть його в текстовий файл такому форматі (список):
 "[дата створення запиту]"
1. [назва валюти 1] to UAH: [значення курсу до валюти 1]
2. [назва валюти 2] to UAH: [значення курсу до валюти 2]
3. [назва валюти 3] to UAH: [значення курсу до валюти 3]
...
n. [назва валюти n] to UAH: [значення курсу до валюти n]


P.S.не забувайте про DRY, KISS, SRP та перевірки
"""
import requests
from datetime import datetime


def check_request(url, content_type):
    """
    The response to the url request is being checked. If the status of the response is within 200s and the type of
    content corresponds to the one specified in the arguments, the function returns the response. Otherwise None.
    :param url:
    :type url: str
    :param content_type: The value should correspond to the 'Content-Type' from the headers of the response.
    :type content_type: str
    :return: A response received from the server that satisfies our requirements.
    :rtype: requests.models.Response|None
    """
    try:
        resp = requests.get(url)
    except Exception as e:
        print(e)
    else:
        if 300 > resp.status_code >= 200:
            if resp.headers.get('Content-Type') == content_type:
                return resp
        return None


def get_str(my_dict, date):
    """
    Accepts a dictionary with a list of currencies and the request date.
    Forms a string with the given information in the required form.
    :param my_dict:
    :type my_dict: dict
    :param date:
    :type date: datetime.datetime
    :return:
    :rtype: str
    """
    dict_stringify = ''
    for i in range(len(my_dict)):
        dict_stringify += f'\n{i+1}. {my_dict[i]["cc"]} to UAH: {my_dict[i]["rate"]}'
    return str(date.date()) + dict_stringify


if __name__ == '__main__':
    URL = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date={}&json'
    my_date = datetime.today()
    response = check_request(URL.format(my_date.strftime("%Y%m%d")), 'application/json; charset=utf-8')
    if response:
        response_json = response.json()
        if len(response_json) == 1 and response_json[0].get('message'):
            raise ValueError('Wrong parameters format in request')
        my_str = get_str(response_json, my_date)
        # print(my_str)
        with open('list.txt', 'w') as file:
            file.write(my_str)
