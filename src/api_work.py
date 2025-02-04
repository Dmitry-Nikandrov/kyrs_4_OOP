from abc import ABC, abstractmethod

import requests


class ApiAbs(ABC):

    @abstractmethod
    def get_connect_api(self):
        """устанавливает соединение с внешним ресурсом и проверяет его статус"""

        pass

    @abstractmethod
    def cast_to_object_list(self, keyword):
        """получает список вакансий с внешнего ресурса и преобразовывает их в объект питона"""

        pass


class Api(ApiAbs):
    """подключается к внешнему ресурсу hh и получает данные о вакансиях, преобразует в объект питона"""

    __params: dict
    vacancies: list

    def __init__(self):
        self.__params = {
            "page": 0,
            "per_page": 100,
            "text": "",
            "only_with_salary": True,
        }
        self.vacancies = []

    def __get_connect_api(self):
        """устанавливает соединение с внешним ресурсом и проверяет его статус"""

        url = "https://api.hh.ru/vacancies"
        response = requests.get(url)
        if response.status_code == 200:
            return f"Подключение успешное. Статус код {response.status_code}"
        return f"Не удалось подключить к ресурсу, response.status_code - {response.status_code}"

    def get_connect_api(self):
        """транслирует работу с приватным методом в эксземлярах класса"""

        return self.__get_connect_api()

    def cast_to_object_list(self, keyword=""):
        """получает список вакансий с внешнего ресурса и преобразовывает их в объект питона"""

        self.get_connect_api()
        url = "https://api.hh.ru/vacancies"
        self.__params["text"] = keyword
        response = requests.get(url, params=self.__params)
        return response.json()["items"]
