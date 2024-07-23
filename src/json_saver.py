import json

from src.json_saver_ABC import JSONSaverABC
from src.vacancy import Vacancy


class JSONSaver(JSONSaverABC):
    """
    Класс для сохранения данных в формате JSON
    """

    def __init__(self, name):
        """
        Функция инициализации
        """
        self.name = name


    def get_data(self):
        """
        Функция для чтения файла в формате JSON
        """
        with open(f'data/{self.name}', "r") as file:
            return json.load(file)


    def save_data(self, data):
        """
        Функция для сохранения данных в файл формата JSON
        """
        with open(f'data/{self.name}', "w") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


    def delete_data(self):
        """
        Функция для удаления данных из файла
        """
        with open(f'data/{self.name}', "w") as file:
            json.dump({}, file)
