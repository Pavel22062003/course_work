import requests
import json


def getting_operations():
    """
    Функция получает вложенный словарь опеаций
    """
    with open('operation.json', 'rt',encoding="UTF-8") as file:
        data = json.load(file)
        return data








