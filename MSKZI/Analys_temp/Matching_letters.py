import requests
import json

def generate_frequency_dict_and_write_to_file():
    write_dict_to_file(generate_frequency_dict())

def write_dict_to_file(temp_list:dict):
    with open("WAR_AND_WORLD.json", 'w', encoding="UTF-8") as json_file:
        json.dump(temp_list, json_file, ensure_ascii=False)

def generate_frequency_dict(question:int,txt:str = None) -> dict:
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя '
    if txt is None:
        #question = int(input("open(1) close(2): "))
        if question == 2:
            txt = "ЫЛЖФСХХНЙМЕЙФЙЭТДСМДСХАЫЛЦХЖМЫЕЭЫДЖЧРСЙЫЬМДМФЙДЙМБНАТЬЗЙТСМЦ\
ЯЙХОМКСБЦЕСЫХЦМБМЬФДСШМТЭЯЖШМЫЦТХ ЖМЫБЙФДЖЧРЖЬМФЙДЖМЭЫЙЬХХЖЬ\
МЫДЦТОВЬРСУСМТЦЗДЖУСМЦДЖГУТЙХХЖЬМТЙЫЦУМЗЦФЦАЖМСВЬРХНЙМБСТТНМ\
ХЖМЗФЭАЦУМИЙФЙАЭМАЖФФСЫМБМЫБЦЙГМДФЖЫХЦГМЫМЦФЖХКЙБНУМЮЭЮЖГДЙМ\
ЕФЙЗЫЛЖБТЬТСМЫЦИЦГМЬФДЭЧМДЖФЛСХЭ"
        if question == 1:
            txt = "СТАРИННЫЕ  ПЕРЕУЛКИ  КИНГСТОНА  СПУСКАЮЩИЕСЯ  К  РЕКЕ  ВЫГЛЯДЕЛИ  О\
ЧЕНЬ  ЖИВОПИСНО  В  ЯРКИХ  ЛУЧАХ  СОЛНЦА  СВЕРКАЮЩАЯ  РЕКА  УСЕЯННАЯ\
  СКОЛЬЗЯЩИМИ  ЛОДКАМИ  ОКАЙМЛЕННАЯ  ЛЕСОМ  ДОРОГА  ИЗЯЩНЫЕ  ВИЛЛЫ\
НА  ДРУГОМ  БЕРЕГУ  ГАРРИС  В  СВОЕЙ  КРАСНОЙ  С  ОРАНЖЕВЫМ  ФУФАЙКЕ\
ПРЕДСТАВЛЯЛИ  СОБОЙ  ЯРКУЮ  КАРТИНУ"

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

def generate_notepad_from_two_lists(letter_list_final: list, lst_letter_frequency: list) -> dict:
    return {k: v for v, k in zip(lst_letter_frequency, letter_list_final)}

if __name__ == '__main__':
    list_temp = sorted(generate_frequency_dict(2).items(), key=lambda x:x[1], reverse=True)
    dict_final:dict = {}
    letter_list_final = []
    for i in range(len(list_temp)):
        dict_final[list_temp[i][0]] = list_temp[i][1]
    for i in dict_final:
        letter_list_final.append(i)


    list_temp = sorted(generate_frequency_dict(1).items(), key=lambda x:x[1], reverse=True)
    dict_open = dict()
    letter_list_open = []
    for i in range(len(list_temp)):
        dict_open[list_temp[i][0]] = list_temp[i][1]
    for i in dict_open:
        letter_list_open.append(i)

    job_dict: dict = generate_notepad_from_two_lists(letter_list_final, letter_list_open)

    for i in job_dict:
        print(i," : ", job_dict[i])