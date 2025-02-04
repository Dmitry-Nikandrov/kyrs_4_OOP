import json
import os
from abc import ABC, abstractmethod

from src.api_work import Api
from src.vacancies_work import Vacancies


class VacanciesEditAbs(ABC):

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def append_data(self, data):
        pass


class VacanciesEdit(VacanciesEditAbs):

    def __init__(self, filename="data.json"):
        self.__filename = filename

    def get_data(self, word=""):
        """получает данные с платформы hh, преобразует их в объект питона и записывает в файл"""

        data_json = Api().cast_to_object_list(keyword=word)
        list_class_atr = []
        for i in data_json:
            vac_comp = Vacancies(
                name=i["name"],
                employer=i["employer"]["name"],
                area=i["area"]["name"],
                salary=i["salary"]["to"],
                requirement=i["snippet"]["requirement"],
            )
            dict_append = {
                "name": vac_comp.name,
                "employer": vac_comp.employer,
                "area": vac_comp.area,
                "salary": vac_comp.salary,
                "requirement": vac_comp.requirement,
            }
            list_class_atr.append(dict_append)

        path = os.path.abspath("./data")
        with open(os.path.join(path, self.__filename), "w", encoding="utf-8") as file:
            json.dump(list_class_atr, file, indent=4, ensure_ascii=False)
            print(
                f"Список вакансий успешно сформирован о сохранен в файл {self.__filename}"
            )
            return list_class_atr

    def append_data(self, vacancy, answer):
        """добавляет новые вакансии в файл базовый файл с вакансиями"""
        if answer.lower() == "да":
            path = os.path.abspath("./data")
            with open(
                os.path.join(path, self.__filename), "r", encoding="UTF-8"
            ) as file:
                data = json.load(file)
                repeat_vac = 0
                for i in data:
                    vac_i = Vacancies(
                        name=i["name"],
                        employer=i["employer"],
                        area=i["area"],
                        salary=i["salary"],
                        requirement=i["requirement"],
                    )
                    if vacancy == vac_i:
                        repeat_vac += 1
                if repeat_vac == 0:
                    dict_to_add = {
                        "name": vacancy.name,
                        "employer": vacancy.employer,
                        "area": vacancy.area,
                        "salary": vacancy.salary,
                        "requirement": vacancy.requirement,
                    }
                    data.append(dict_to_add)
                    new_list = data

            if repeat_vac == 0:
                print(
                    f"""
Добавлена вакансия:

Название должности - {vacancy.name},
Работадатель: {vacancy.employer},
Страна: {vacancy.area},
Заработная плата: {vacancy.salary},
Требования: {vacancy.requirement}"""
                )
                path = os.path.abspath("./data")
                with open(
                    os.path.join(path, self.__filename), "w", encoding="UTF-8"
                ) as file:
                    file.write(json.dumps(new_list, ensure_ascii=False, indent=4))
                    return "Успешное добавление вакансии в файл JSON"
            else:
                return "Вакансия не добавлена"

    def delete_data(self, answer):
        """очищает файл с вакансиями"""

        if answer.lower() == "да":
            path = os.path.abspath("./data")
            with open(
                os.path.join(path, self.__filename), "w", encoding="utf-8"
            ) as file:
                file.write("")
                return "удалены данные в файле data.json"


def search_in_vacancies(vacancies_list, search_word=",jkty"):
    """ищет ключевые слова в файле с вакансиями и выдает отфильтрованные данные"""

    # search_word = input("Введите ключевые слова для фильтрации вакансий: ")
    search_list = [
        x
        for x in vacancies_list
        if any(
            [
                search_word in x["area"] if x["area"] is not None else 0,
                search_word in x["requirement"] if x["requirement"] is not None else 0,
                search_word in x["employer"] if x["employer"] is not None else 0,
            ]
        )
    ]
    return search_list


def salary_range(list_vacancies, min_sal, max_sal):
    """фильтрует ваксансии по заданному диапозону заработной платы"""

    return list(filter(lambda x: min_sal <= x["salary"] <= max_sal, list_vacancies))


def sort_salary(list_vacancies):
    """выводит заданное количество вакансий среди отсортированного по зарплате списка вакансий"""

    top_n = 3  # int(input("Введите количество вакансий для вывода в топ N: "))
    return sorted(list_vacancies, key=lambda x: x["salary"], reverse=True)[0:top_n]
