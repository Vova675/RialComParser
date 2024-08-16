from baseFunc import get_sep_channel
from parser.parser import ParserClass
from excelmaker.excelmaker import ExcelFileMakerClass
from formatters.formatters import InternetApartmentFormatterClass, InternetPrivatHouseFormatterClass, InternetTVApartmentFormatterClass, InternetTVPrivatHouseFormatterClass

def start_parsing():
    """
    Получение данных с сайта\n
    Возращает список таблиц
    """
    parser = ParserClass()
    parser.parse_tables_data()
    return parser.get_tables()

def create_excel_file(parsing_data):
    """
    Создание excel файла из данных полученых парсером\n
    parsing_data - список данных полученых парсером
    """
    internet_apartment_data = parsing_data[0]
    internet_TV_apartment_data = parsing_data[1]
    internet_privat_house_data = parsing_data[2]
    internet_TV_privat_house_data = parsing_data[3]

    name_and_channel_list = get_sep_channel(internet_TV_apartment_data)

    internet_apartment_obj = InternetApartmentFormatterClass()
    internet_apartment_obj.set_data(internet_apartment_data)
    internet_TV_apartment_obj = InternetTVApartmentFormatterClass()
    internet_TV_apartment_obj.set_data(internet_TV_apartment_data, name_and_channel_list)
    internet_privat_house_obj = InternetPrivatHouseFormatterClass()
    internet_privat_house_obj.set_data(internet_privat_house_data)
    internet_TV_privat_house_obj = InternetTVPrivatHouseFormatterClass()
    internet_TV_privat_house_obj.set_data(internet_TV_privat_house_data, name_and_channel_list)

    table = []
    table.extend(internet_apartment_obj.get_data()) 
    table.extend(internet_TV_apartment_obj.get_data())
    table.extend(internet_privat_house_obj.get_data())
    table.extend(internet_TV_privat_house_obj.get_data())

    excel_maker = ExcelFileMakerClass()
    excel_maker.create_file(table)

if __name__ == '__main__':
    parsing_data = start_parsing()
    create_excel_file(parsing_data)
    
    
    
