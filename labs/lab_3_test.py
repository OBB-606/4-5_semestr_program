import sys
import csv
import time as t
from math import inf

time_start = t.time()

with open("adj_list_lab_1_for_3_new_type.csv", mode='r', encoding="utf-8") as r_file:
    file_reader = csv.reader(r_file, delimiter=",", quoting=csv.QUOTE_MINIMAL)
    Adj_list = []
    for row in file_reader:
        Adj_list.append(row)

size = len(Adj_list)
Adj_list_final = [[int(j) for j in i] for i in Adj_list]

Matrix = []
Matrix_helper = []

for i in range(size):
    Matrix_helper.append([0] * size)

for i in range(size):
    Matrix.append([0] * size)

for i in range(len(Adj_list_final)):
    for j in range(0, len(Adj_list_final[i]) - 1, 2):
        edge_temp = Adj_list_final[i][j]
        weight_temp = Adj_list_final[i][j + 1]
        Matrix[i][edge_temp] = weight_temp
iz = sys.maxsize  # бесконечность
Matrix = [
    [iz, 4, iz, iz, iz, 4],
    [4, iz, 2, 5, iz, 4],
    [iz, 2, iz, 3, 5, 6],
    [iz, 5, 3, iz, 1, 4],
    [iz, iz, 5, 1, iz, 3],
    [4, 4, 6, 4, 3, iz]
]
Matrix_helper = []
for i in range(len(Matrix)):
    Matrix_helper.append([sys.maxsize] * len(Matrix))

# for i in range(len(Matrix_helper)):
# print(Matrix_helper[i])


i_temp = 0
j_temp = 0
value_temp = sys.maxsize
counter = 0

min_element_i = []
min_element_j = []


# def printer():
# print(len(Matrix))

def search_min_element():
    global i_temp, j_temp, value_temp, Matrix, Matrix_helper
    for i in range(len(Matrix)):
        for j in range(len(Matrix[i])):
            if Matrix[i][j] < value_temp:
                value_temp = Matrix[i][j]
                i_temp = i
                j_temp = j
    min_element_i.append(i_temp)
    min_element_j.append(j_temp)
    value_temp = sys.maxsize
    first_delete_string()


def first_delete_string():
    for i in range(len(Matrix)):
        Matrix[i_temp][j] = sys.maxsize
        Matrix[j_temp][j] = sys.maxsize
    first_add_in_second_matrix()


def first_add_in_second_matrix():
    for i in range(len(Matrix_helper)):
        Matrix_helper[i][i_temp] = Matrix[i][i_temp]
    for j in range(len(Matrix_helper)):
        Matrix_helper[j][j_temp] = Matrix[j][j_temp]
    search_min_in_second_matrix()


def search_min_in_second_matrix():
    global i_temp, j_temp, value_temp, counter

    for i in range(len(Matrix_helper)):
        for j in range(len(Matrix_helper[i])):
            if Matrix_helper[i][j] < value_temp:
                value_temp = Matrix_helper[i][j]
                i_temp = i
                j_temp = j
                counter += 1

    if (value_temp < sys.maxsize):
        min_element_j.append(j_temp)
        min_element_i.append(i_temp)

    for j in range(len(Matrix_helper)):
        Matrix_helper[i_temp][j] = sys.maxsize
    value_temp = sys.maxsize

    if counter > 1 or counter == 1:
        counter = 0
        delete_and_add()
    else:
        for i in range(len(min_element_j)):
            print('\t', min_element_i[i], " ", min_element_j[i], "  ")


def delete_and_add():
    for j in range(len(Matrix)):
        Matrix[i_temp][j] = sys.maxsize
    for i in range(len(Matrix_helper)):
        Matrix_helper[i][i_temp] = Matrix[i][i_temp]
    search_min_in_second_matrix()


# for i in range(len(Matrix)):
# print(Matrix[i])

search_min_element()
time_running_program = t.time() - time_start
print("program running time is ", round(time_running_program, 4), "seconds")
