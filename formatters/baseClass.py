class BaseClass:

    def __init__(self):
        """
        Базовый класс\n
        __data - поле для хранения данных
        """
        self.__data = []

    def get_data(self):
        return self.__data

    def set_data(self, data):
        return 0