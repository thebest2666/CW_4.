# Создание экземпляра класса для работы с API сайтов с вакансиями
from src.hhAPI import HeadHunterAPI
from src.json_saver import JSONSaver
from src.utils import filter_vacancies, sort_vacancies, get_vacancies_by_salary, get_top_vacancies, print_vacancies
from src.vacancy import Vacancy


# Функция для взаимодействия с пользователем
def user_interaction():
    """
    Функция взаимодействия с пользователем
    """
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат: ")  # Пример: 100000 - 150000

    hh_api = HeadHunterAPI()

    # Получение вакансий с hh.ru в формате JSON
    hh_vacancies = hh_api.get_vacancies(search_query)

    # Преобразование набора данных из JSON в список объектов
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

    json_saver = JSONSaver('vacancies.json')
    json_saver.save_data(hh_vacancies)

    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()
