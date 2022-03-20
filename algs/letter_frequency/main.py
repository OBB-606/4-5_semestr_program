from random import shuffle

def generate_notepad() -> dict:
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя' + 'абвгдежзийклмнопрстуфхцчшщъыьэюя'.upper()
    alphabet_cpy = shuffle_string(alphabet)

    return {c1: c2 for c1, c2 in zip(alphabet, alphabet_cpy)}

def shuffle_string(txt:str) ->str:
    txt_lst = list(txt)
    shuffle(txt_lst)
    return ''.join(txt_lst)

def encrypt(text: str, notepad:dict = None) ->str:
    if notepad is None:
        notepad = generate_notepad()
        print("Notepad is: ", notepad, sep='\n')
    return ''.join([notepad.get(c, c) for c in text])

def decrypt(text:str, notepad:dict) -> str:
    notepad_reversed = {v: k for k, v in notepad.items() }
    return encrypt(text, notepad_reversed)

if __name__ == '__main__':
    a = encrypt("Шифруем какой нибудь текст")
    print(a)