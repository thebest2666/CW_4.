import requests

from src.ABChhAPI import HeadHunterAPI_ABC
from src.settings import HH_URL


class HeadHunterAPI(HeadHunterAPI_ABC):
    """
    Класс для взаимодействия с HH через API
    """
    pass

    def __init__(self):
        """
        Функция инициализации
        """
        self.__url = HH_URL
        self.__params ={"page": 0, "per_page": 100}

    def get_vacancies(self, name):
        """
        Функция для получения данных с HH
        """
        data = self.connect_hh(name).json()
        return data

    def connect_hh(self, name):
        """
        Функция для получения данных с HH по определенным параметрам
        """
        response = requests.get(f"{self.__url}&text={name}", params=self.__params)
        return response





