class Vacancy():
    """
    Класс для работы с вакансиями
    """

    def __init__(self, id, name, url, salary):
        """
        Функция инициализации
        """
        self.id = id
        self.name = name
        self.url = url
        self.salary = salary


    @classmethod
    def cast_to_object_list(cls, json_vacancies):
        vacancies_list =[]
        for v in json_vacancies["items"]:
            if v["salary"] is None:
                salary = 0
            elif v["salary"]["from"] is None and v["salary"]["to"] is not None:
                salary = v["salary"]["to"]
            elif v["salary"]["from"] is not None and v["salary"]["to"] is None:
                salary = v["salary"]["from"]
            else:
                salary = (v["salary"]["from"]+v["salary"]["to"])/2
            vacancies_list.append(cls(id=v["id"], name=v["name"], url=v["url"], salary=salary))
        return vacancies_list


    def __lt__(self, other):
        """
        Магический метод для сравнения объектов
        """
        return self.salary < other.salary


    def __str__(self):
        """
        Магический метод для строкового представления объекта
        """
        return f"""Название вакансии: {self.name}, 
Ссылка на вакансию: {self.url},
Заработная плата: {self.salary}"""

