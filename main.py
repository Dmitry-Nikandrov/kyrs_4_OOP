from src.file_work import VacanciesEdit
from src.utils import (range_salary, search_in_vacancies, sort_salary,
                       vac_to_append)

if __name__ == "__main__":
    search_vacancy = input("Введите профессию для поиска вакансий на hh.ru: ")
    vacancies_list = VacanciesEdit().get_data(search_vacancy)
    search_word = input("\nВведите ключевое слово для фильтрации вакансий: ")
    search_vacancies = search_in_vacancies(vacancies_list, search_word)
    salary_min = int(
        input("\nВведите минимальный размер зарплаты для фильтрации вакансий: ")
    )
    salary_max = int(
        input("Введите максимальный размер зарплаты для фильтрации вакансий: ")
    )
    filted_salary = range_salary(
        search_vacancies, min_sal=salary_min, max_sal=salary_max
    )
    top_n = int(input("\nВведите топ вакансий для ввода на экран: "))
    sort_list = sort_salary(filted_salary, top_n)
    add_word = input("\nДобавить новую вакансию в список (да/нет): ")
    add_vacancies = VacanciesEdit().append_data(vac_to_append, add_word)
    delete_word = input("\nОчистить список вакансий (да/нет): ")
    VacanciesEdit().delete_data(delete_word)
