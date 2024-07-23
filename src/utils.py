def filter_vacancies(list_vacancies, words):
    """
    Функция фильтрации вакансий
    """
    list_filter_vacancies = []
    for vacancy in list_vacancies:
        for word in words:
            if word.lower() in vacancy.name.lower():
                list_filter_vacancies.append(vacancy)
                break
    return list_filter_vacancies


def get_vacancies_by_salary(list_vacancies, salary_range):
    """
    Функция фильтрации вакансий по заработной плате
    """
    list_filter_vacancies = []
    salary_from, salary_to = salary_range.split("-")
    for vacancy in list_vacancies:
        if int(salary_from) <= vacancy.salary <= int(salary_to):
            list_filter_vacancies.append(vacancy)
    return list_filter_vacancies


def sort_vacancies(list_vacancies):
    """
    Функция сортировки вакансий
    """
    return sorted(list_vacancies, reverse=True)


def get_top_vacancies(list_vacancies, top):
    """
    Функция для получения приоритетных вакансий
    """
    return list_vacancies[:top]


def print_vacancies(list_vacancies):
    """
    Функция для отображения приоритетных вакансий
    """
    for vacancy in list_vacancies:
        print(vacancy)
        print("-" * 50)
