import csv
import time
"Позволяет получать из csv список смежности" \
"где нечетные элементы - смежная вершина, а четные - вес ребра, их соединяющего" \
"Далее преобразует это в список смежности из кортежей. Порядок элементов в кортеже сохраняется"
time_start = time.time()

with open ("adj_list_lab_1_for_3_new_type.csv", mode = 'r', encoding = "utf-8")as r_file:
    file_reader = csv.reader(r_file,delimiter =";",quoting=csv.QUOTE_MINIMAL)
    Adj_list = []
    for row in file_reader:
        Adj_list.append(row)
size = len(Adj_list)
Adj_list_final = [[int(j) for j in i]for i in Adj_list]
Adj_list_tuples = []

for i in range(size):
    Adj_list_tuples.append([])



for i in range(len(Adj_list_final)):
    for j in range(0, len(Adj_list_final[i])-1, 2):
        temp_tuple = (Adj_list_final[i][j], Adj_list_final[i][j+1])
        Adj_list_tuples[i].append(temp_tuple)

for i in range(len(Adj_list_tuples)):
    print(Adj_list_tuples[i])












time = time.time() - time_start
print(round(time,4))