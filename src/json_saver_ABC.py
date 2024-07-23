from abc import ABC, abstractmethod


class JSONSaverABC(ABC):
    """
    Абстрактный класс для сохранения данных в формате JSON
    """

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def save_data(self, data):
        pass

    @abstractmethod
    def delete_data(self):
        pass