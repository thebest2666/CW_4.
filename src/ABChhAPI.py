from abc import ABC, abstractmethod


class HeadHunterAPI_ABC(ABC):
    """
    Абстрактный класс для взаимодействия с HH через API
    """


    @abstractmethod
    def connect_hh(self, name):
        pass

    @abstractmethod
    def get_vacancies(self, name):
        pass

