import regex as re

def get_num_from_str(str):
    result = re.findall(r'\d{2,}', str)
    return int(result[0]) 

def get_sep_channel(data):
    name_and_channel_list = []
    for i in range(1, len(data)):
        name = re.findall(r'\D[^(]{0,}', data[i][0])[0]
        channel = get_num_from_str(data[i][0])
        name_and_channel_list.append([name, channel])
    return name_and_channel_list