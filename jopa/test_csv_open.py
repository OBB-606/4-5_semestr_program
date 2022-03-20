import csv
import time

start_time = time.time()
with open ("adj_list_lab_1_for_3_new_type.csv", mode = 'r', encoding = "utf-8",)as r_file:
    file_reader = csv.reader(r_file,delimiter =";",quoting=csv.QUOTE_MINIMAL)
    Adj_list = []
    for row in file_reader:
        Adj_list.append(row)
size = len(Adj_list)
Adj_list_final =[]

for i in range(size):
    Adj_list_final.append([])
#Существует два варианта расположения двузначного числа в кортеже: на первой позиции, на второй и на обеих.
#Если двузначного числа вообще нет в кортеже, то выполняется первый блок в цикле, из Adj_list получаются элементы под индексами [i][j][1] and [i][j][4],
#помещаются в темпоральный кортеж, парсятся в integer и потом помещаются в финальный список смежности.
#Если ловится исключение ValueError, значит было встречено двузначное число и под индексом [i][j][4] находится скобка, а ее никак не запарсить в integer.
#Поэтому выцепляется целый элемент списка строк (типа (8, 1)) и
#
#
#
#
#
#
#
for i in range (len(Adj_list)):
    for j in range(len(Adj_list[i])):
        try:
            a = Adj_list[i][j][1]
            b = Adj_list[i][j][4]
            temp_tuple = (int(a), int(b))
            Adj_list_final[i].append(temp_tuple)
        except ValueError:
            try:
                str = Adj_list[i][j]
                str_temp_first = int(str[1]+str[2])
                #a = str_temp_first
                b = int(Adj_list[i][j][5])
                temp_tuple = (str_temp_first, b)
                Adj_list_final[i].append(temp_tuple)
                if Adj_list[i][j][1]:
                    pass
            except ValueError:
                try:
                    str = Adj_list[i][j]
                    str_temp_second = int(str[5]+str[6])
                    a = int(Adj_list[i][j][1])
                    temp_tuple = (a, str_temp_second)
                    Adj_list_final[i].append(temp_tuple)
                except ValueError:
                    try:
                        str = Adj_list[i][j]
                        str_temp_first = int(str[1] + str[2])
                        str_temp_second = int(str[5] + str[6])
                        temp_tuple = (str_temp_first, str_temp_second)
                        Adj_list_final[i].append(temp_tuple)
                    except ValueError:
                        pass


for i in range (size):
    print(Adj_list_final[i])
time = time.time() - start_time
print(round(time, 4))
