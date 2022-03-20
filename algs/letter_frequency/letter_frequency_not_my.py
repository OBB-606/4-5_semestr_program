import requests
import json

def generate_frequency_dict_and_write_to_file():
    write_dict_to_file(generate_frequency_dict())

def write_dict_to_file(temp_list:dict):
    with open("WAR_AND_WORLD.json", 'w', encoding="UTF-8") as json_file:
        json.dump(temp_list, json_file, ensure_ascii=False)

def generate_frequency_dict(txt:str = None) -> dict:
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    if txt is None:
        response = requests.get("http://az.lib.ru/t/tolstoj_lew_nikolaewich/text_0073.shtml")
        txt = response.text
    letter_list = [i.lower() for i in txt if i.lower() in alphabet]
    # print(letter_list[0:1000])

    temp_list: dict = {}

    for i in letter_list:
        if i not in temp_list:
            temp_list[i] = 1
        else:
            temp_list[i] += 1
    # Эквивалентная запись заполнения словаря частотами:
    # for i in letter_list:
    #     temp_list[i] = temp_list.get(i, 0) + 1
    return temp_list

def generate_list_for_frequency_analyse(temp_list:dict = None):
    if temp_list is None:
        with open("WAR_AND_WORLD.json", 'r', encoding="UTF-8") as json_file:
            temp_list = json.load(json_file)

    return sorted(temp_list.items(), key=lambda x:x[1], reverse=True)
#print(generate_list_for_frequency_analyse())

if __name__ == '__main__':
    generate_frequency_dict_and_write_to_file()
