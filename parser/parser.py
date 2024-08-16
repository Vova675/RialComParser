from bs4 import BeautifulSoup
import requests
from config import url

class ParserClass:

    def __init__(self):
        self.__url = url
        self.__Tables_data = []
        self.__page = requests.get(self.__url)
        if self.__page.status_code != 200:
            print('Error')
        self.__soup = BeautifulSoup(self.__page.text, "html.parser")

    def __find_tables(self):
        self.__Tables_list = self.__soup.find_all(
        "table", 
        class_=[
            "table table-sm table-striped table-borderless table-responsive", 
            "table table-sm table-striped table-borderless table-responsive-sm"])
        return 0
    
    def parse_tables_data(self):
        self.__find_tables()
        for table in self.__Tables_list:
            tr_list = table.find_all("tr")
            Table_data = []
            for tr in tr_list:
                th_list = tr.find_all("th")
                td_list = tr.find_all("td")
                size = len(th_list) if (len(td_list) == 0) else len(td_list)
                col = []
                j = 0
                for j in range(0, size):
                    col.append(th_list[j].string if (len(td_list) == 0) else td_list[j].string)
                    j += 1
                Table_data.append(col)
            self.__Tables_data.append(Table_data)
        return 0
    
    def get_tables(self):
        return self.__Tables_data

    def set_table(self, table):
        self.__Tables_data = table
        return 0