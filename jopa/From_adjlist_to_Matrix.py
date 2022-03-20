import csv
import time as t

time_start = t.time()

with open ("adj_list_lab_1_for_3_new_type.csv", mode = 'r', encoding = "utf-8",)as r_file:
    file_reader = csv.reader(r_file,delimiter =";",quoting=csv.QUOTE_MINIMAL)
    Adj_list = []
    for row in file_reader:
        Adj_list.append(row)
size = len(Adj_list)
Adj_list_final = [[int(j) for j in i]for i in Adj_list]

Matrix = []
for i in range(size):
    Matrix.append([0]*size)

for i in range(len(Adj_list_final)):
    for j in range(0, len(Adj_list_final[i])-1, 2):
        edge_temp = Adj_list_final[i][j]
        weight_temp = Adj_list_final[i][j+1]
        Matrix[i][edge_temp] = weight_temp
for i in range(len(Matrix)):
    print(Matrix[i])
count_edge = 0
#for i in range(len(Matrix)):
    #for j in range(len(Matrix[i])):
        #if Matrix[i][j] != 0:
            #count_edge += 1
#print("count vertex is ", len(Matrix))
#print("count edges is ", count_edge/2)
time_running_program = t.time() - time_start
print("program running time is ", round(time_running_program, 4), "seconds")