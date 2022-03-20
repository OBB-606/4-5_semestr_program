import random

word = "Окунев Валерий Витальевич ИСБ-119"
print("Word: ", word)
id_array = []

for i in range(len(word)):
    id_array.append(i)

id_array_double = list(id_array)
id_word_dict = dict()
k = 0

for i in word:
    id_word_dict[k] = i
    k+=1

word_encoding = ""
def random_shuffle():
    global word_encoding
    try:
        for i in range(len(id_word_dict)-1):
            random_id = random.choice(id_array)
            id_array.remove(random_id)
            temp_letter = id_word_dict[random_id]
            word_encoding += temp_letter
    except KeyError:
            random_shuffle()

random_shuffle()
print("encoding: ", word_encoding)

word_decoding = ""
for i in id_array_double:
    word_decoding += id_word_dict[i]
print("decoding:", word_decoding)