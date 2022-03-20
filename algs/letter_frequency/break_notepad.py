from letter_frequency_not_my import generate_list_for_frequency_analyse, generate_frequency_dict
from main import encrypt
#print(generate_list_for_frequency_analyse())

def break_notepad(text:str) -> str:
    # temp_list = generate_frequency_dict(text)
    # list_from_text = generate_list_for_frequency_analyse(temp_list)
    # return list_from_text
    lst= generate_list_for_frequency_analyse()
    lst_from_txt = generate_list_for_frequency_analyse(generate_frequency_dict(text))

    notepad = generate_notepad_from_two_lists(lst, lst_from_txt)
    print(notepad)
    return encrypt(text, notepad)

def generate_notepad_from_two_lists(lst_1:list, lst_2:list)-> dict:
    d = {}
    print(lst_1)
    print(lst_2)

    return {k: v for v, k in zip(lst_1, lst_2)}

a = "ИЬЭЛЬЕТЦЫЭГМВЬЫГТЫЖЦЭЗЦЫЭГВЭИЖЫЭГКГВКЧЫЭГЦЫГЯГЯЫРЩМЧЭГЗМЯТВЯ\
МЭВТБГЦЕЬЕТВЕФОЭЭГЯЫЖЦЭЦКЭГЛЫЬЫЖЙГКЫЕЦЦГТВЫКВГЯГЩЕЦЛЬЕЮВГЧЫЖ\
ЖЭГКГЯЭТЙГЩЭЦЙГЦЕЛЕЦМЦЭГНЫЬЫЩЫЛГЫНЖЕАЕЖТБГПЬБ ЕЦКЭСГЫЬМХКБГК\
ГТВМЛЫСГЛЫИУВГИЫГСЫТВЫЯЫДГЛЬКЛЫСГЛЫСЕЦЩКЬЫЯГИЬЫЛЖБВКБСКГКГНЬ\
МПУСКГАМВЛЕСКГПЫЬЫЩЕВУЧГЖМЗЦКЛЫЯ"

print(break_notepad(a))