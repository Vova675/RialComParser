import openpyxl 
from openpyxl.styles import Font
from config import header, width_list, excel_file_name

class ExcelFileMakerClass:

    def __init__(self):
        """
        Создает выходной excel файл\n
        Использует header из файла config.py как шапку таблицы\n
        Использует width_list из файла config.py как параметры шапки\n
        Использует excel_file_name из файла config.py как имя выходного файла excel\n
        __workbook - рабочий файл
        __sheet - рабочий лист
        """
        self.__workbook = openpyxl.Workbook() 
        self.__sheet = self.__workbook.active
        self.__sheet.append(header)

    def __set_param(self):
        """
        Задает параметры шапки
        """
        self.__sheet.column_dimensions['A'].width = width_list[0]
        self.__sheet.column_dimensions['B'].width = width_list[1]
        self.__sheet.column_dimensions['C'].width = width_list[2]
        self.__sheet.column_dimensions['D'].width = width_list[3]
        for i in range(1, 5):
            self.__sheet.cell(row = 1, column = i).font = Font(size = 12, bold = True)
        return 0

    def __set_table(self, table):
        """
        Записывает данные в таблицу excel\n
        table - список данных (таблица)
        """
        for row in table:
            self.__sheet.append(row)
        return 0

    def create_file(self, table):
        """
        Записывает данные в таблицу\n
        Устанавливает параметры шапки\n
        Сохраняет выходной файл 
        """
        self.__set_table(table)
        self.__set_param()
        self.__workbook.save(excel_file_name)
        return 0