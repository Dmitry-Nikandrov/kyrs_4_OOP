from typing import Union


class Vacancies:
    """реализует функциональности по работе с вакансиями"""

    __slots__ = ("name", "employer", "area", "salary", "requirement")

    name: str
    employer: str
    salary: int
    requirement: str

    def __init__(self, name, employer, area, salary, requirement):
        self.name = self.__name(name)
        self.employer = employer
        self.salary = self.__salary(value=salary)
        self.requirement = requirement
        self.area = area

    def __ge__(self, other):
        """сравнивает экземпляры класса Vacancies между собой"""

        if isinstance(other, self.__class__) or other is not None:
            return self.salary >= other.salary
        return "недопустимое сравнение"

    def __gt__(self, other):
        """сравнивает экземпляры класса Vacancies между собой по уровню заработной платы"""

        if isinstance(other, self.__class__) or other is not None:
            return self.salary > other.salary
        return "недопустимое сравнение"

    def __eq__(self, other):
        """сравнивает экземпляры класса Vacancies между собой"""

        return (
            self.name == other.name
            and self.area == other.area
            and self.salary == other.salary
            and self.requirement == other.requirement
        )

    def __salary(self, value: Union[int, None]):
        """валидирует зарплату при ее инициализации"""

        if value is None:
            return 1
        elif value <= 0:
            return 1
        return value

    def __name(self, text):
        """валидирует название вакансии при ее инициализации"""

        if type(text) is not str or text is None:
            print(
                f'Недопустимое название вакансии. Значение атрибута name исправлено на "НЕОПРЕДЕЛЕНО"'
            )
            return "НЕОПРЕДЕЛЕНО"
        return text
