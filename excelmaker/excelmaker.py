import openpyxl 
from openpyxl.styles import Font
from config import header, width_list

class ExcelFileMakerClass:

    def __init__(self):
        """
        привет
        """
        self.__workbook = openpyxl.Workbook() 
        self.__sheet = self.__workbook.active
        self.__sheet.append(header)

    def __set_param(self):
        self.__sheet.column_dimensions['A'].width = width_list[0]
        self.__sheet.column_dimensions['B'].width = width_list[1]
        self.__sheet.column_dimensions['C'].width = width_list[2]
        self.__sheet.column_dimensions['D'].width = width_list[3]
        for i in range(1, 5):
            self.__sheet.cell(row = 1, column = i).font = Font(size = 12, bold = True)
        return 0

    def __set_table(self, table):
        for row in table:
            self.__sheet.append(row)
        return 0

    def create_file(self, table):
        self.__set_table(table)
        self.__set_param()
        self.__workbook.save("table.xlsx")
        return 0