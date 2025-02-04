from src.vacancies_work import Vacancies


def search_in_vacancies(vacancies_list, search_word):
    """ищет ключевые слова в файле с вакансиями и выдает отфильтрованные данные"""

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
    print("Список вакансий успешно отфильтрован")
    return search_list


def range_salary(list_vacancies, min_sal, max_sal):
    """фильтрует вакансии по заданному диапазону заработной платы"""

    print("Список вакансий отобран по заданному диапазону заработной платы")
    return list(filter(lambda x: min_sal <= x["salary"] <= max_sal, list_vacancies))


def sort_salary(list_vacancies, top_n):
    """выводит заданное количество вакансий среди отсортированного по зарплате списка вакансий"""

    list_sorted = sorted(list_vacancies, key=lambda x: x["salary"], reverse=True)
    for i in list_sorted[0:top_n]:
        print(
            f"""
Название должности - {i['name']},
Работадатель: {i['employer']},
Страна: {i['area']},
Заработная плата: {i['salary']},
Требования: {i['requirement']}"""
        )
    return sorted(list_vacancies, key=lambda x: x["salary"], reverse=True)[0:top_n]


vac_to_append = Vacancies("Оператор", "ООО Лютик", "Россия", None, "умеренные")
