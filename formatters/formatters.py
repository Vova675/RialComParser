from .baseClass import BaseClass
from baseFunc import get_num_from_str

class InternetApartmentFormatterClass(BaseClass):

    def __init__(self):
        super().__init__()

    def set_data(self, data):
        for i in range(1, len(data)):
            col = []
            col.append(data[i][0])
            col.append('null')
            col.append(get_num_from_str(data[i][3]) / 1000)
            col.append(get_num_from_str(data[i][1]))
            self._BaseClass__data.append(col)
        return 0

class InternetPrivatHouseFormatterClass(BaseClass):

    def __init__(self):
        super().__init__()

    def set_data(self, data):
        for i in range(1, len(data)):
            col = []
            col = []
            col.append(data[i][0])
            col.append('null')
            col.append(get_num_from_str(data[i][3]) / 1000)
            col.append(get_num_from_str(data[i][1]))
            self._BaseClass__data.append(col)
        return 0

class InternetTVApartmentFormatterClass(BaseClass):

    def __init__(self):
        super().__init__()

    def set_data(self, data, name_and_channel_list):
        header_and_speed_list = []
        for elem in data[0]:
            if elem != ' ':
                header_and_speed_list.append([elem, get_num_from_str(elem)]) 

        for i in range(1, len(data)): 
            for j in range(1, len(data[0])):
                col = []
                col.append(name_and_channel_list[i-1][0] + '+ ' + header_and_speed_list[j-1][0])
                col.append(name_and_channel_list[i-1][1])
                col.append(header_and_speed_list[j-1][1])
                col.append(int(data[i][j]))
                self._BaseClass__data.append(col)
            
        return 0

class InternetTVPrivatHouseFormatterClass(BaseClass):

    def __init__(self):
        super().__init__()

    def set_data(self, data, name_and_channel_list):
        header_and_speed_list = []
        for elem in data[0]:
            if elem != ' ':
                header_and_speed_list.append([elem, get_num_from_str(elem)]) 

        for i in range(1, len(data)): 
            for j in range(1, len(data[0])):
                col = []
                col.append(data[i][0] + '+ ' + header_and_speed_list[j-1][0] + '_ч')
                col.append(name_and_channel_list[i-1][1])
                col.append(header_and_speed_list[j-1][1])
                col.append(int(data[i][j]))
                self._BaseClass__data.append(col)
            
        return 0
