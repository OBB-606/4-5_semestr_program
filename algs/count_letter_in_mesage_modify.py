import time

start_time = time.time()

temp = open("../MSKZI/MSKZI.txt", "r", encoding="ANSI")
data = temp.read()

letter_dict = dict()
temp_array = []

for i in data:#если символ уже содержится в списке уникальных символов, то ничего не делаем
       #Если не содержится - добавляем в список
    if i in temp_array:
        pass
    else:
        temp_array.append(i)

temp_array_2 = []#темпоральный список для работы цикла, из него будут удаляться уже обработанные символы

for i in temp_array:# копирование символов из первого списка во второй
    temp_array_2.append(i)
for i in temp_array:# создание ассоциативного массива, где ключом является символ алфавита сообщения
    letter_dict[i] = 0

k = 0#счетчик
counter = 0#количество символа в сообщении

while len(temp_array_2) != 0:#пока темпоральный список не пуст
    for i in data:
        if i == temp_array[k]:#Если встречается текущий уникальный символ в сообщении, то counter прибавляет единицу
            counter += 1
    letter_dict[temp_array[k]] = counter#символу сопоставляется его количество в сообщении
    temp_array_2.remove(temp_array[k])#из темпорального массива удаляется уже посчитанный символ
    counter = 0#обнуляем counter
    k += 1# переходим на следующий символ алфавита

for i in temp_array:
    print(i, " : ", letter_dict[i])

print("the power of the alphabet of a given message: ", len(temp_array))
print("message length: ", len(data), "symbol's")
time = time.time() - start_time
print('running time program is ->', round(time, 4), '<- seconds')