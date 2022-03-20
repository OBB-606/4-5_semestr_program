import csv
from numpy.random import poisson
import random
import time

start_time = time.time()
Matrix_not_oriented = []
Matrix_oriented = []
count_list = []# cписок, хранящий в себе степени всех вершин
size_matrix = int(input("write size Matrix: "))

for i in range(size_matrix):##создание списков и заполнение их нулями
    Matrix_oriented.append([0]*size_matrix)
    Matrix_not_oriented.append([0]*size_matrix)

def degree_counter(Matrix:list):## метод ищет степень каждой вершины графа
    for i in range(len(Matrix)):
        count = int(0)
        for j in range(len(Matrix)):
            if Matrix[i][j] != 0:
                count+=1
        count_list.append(count)

def csv_creator(adj_list:list, Matrix:list):##метод созданиет csv файл и записывает в него список смежности
    with open("adj_list_lab_1_for_9.csv", "w", newline="",) as csvfile:
        writer = csv.writer(csvfile, delimiter = ';')
        for i in range(len(Matrix)):
            writer.writerow(adj_list[i])

def csv_creator_1(adj_list:list, Matrix:list):##метод созданиет csv файл и записывает в него список смежности БЕЗ ВЕСА
    with open("adj_list_lab_1_for_3_new_type_simple.csv", "w", newline="",) as csvfile:
        writer = csv.writer(csvfile, delimiter = ';')
        for i in range(len(Matrix)):
            writer.writerow(adj_list[i])

print("Oriented(1) / not oriented(2)")
question = int(input())
middle_degree = int(input("Write middle degree: "))

if question==1:## ориентированный
    for i in range(len(Matrix_oriented)):
        for j in range(random.randint(0, middle_degree), middle_degree + (middle_degree//2), 1):
            Matrix_oriented[i][j] = random.randint(0, middle_degree**2)

    #for i in range(len(Matrix_oriented)-1):#соблюдение условия ориентированности, путем целенаправленного
        ##несимметризирования матрицы
        #Matrix_oriented[i] = Matrix_oriented[i+1]
    for i in range(len(Matrix_oriented)):
        for j in range(len(Matrix_oriented)):
            Matrix_oriented[i][i] = 0##заполнение нулями главной диагонали

    degree_counter(Matrix_oriented)
    print(Matrix_oriented)
    result_middle_degreee = sum(count_list)/ size_matrix
    adjacency_list_simple = [[j for j in range(len(Matrix_oriented[i])) if Matrix_oriented[i][j] != 0] for i in
                      range(len(Matrix_oriented))]
    csv_creator(adjacency_list_simple, Matrix_oriented)
    adjacency_list = []

    for i in range (size_matrix):
        adjacency_list.append([])

    for i in range (len(Matrix_oriented)):
        for j in range (len(Matrix_oriented)):
            if Matrix_oriented[i][j] != 0:
                list_temp = (j, Matrix_oriented[i][j])#в темпортальный список помещается индекс вершины с которой смежна текущая вершина
                #и вес ребра, их соединяющего
                adjacency_list[i].append(list_temp[0])
                adjacency_list[i].append(list_temp[1])#в текущую строку(соответствует индексу текущей вершины) списка смежности
                #помещается темпоральный список с индексом и весом
                #таким образом создается список смежности, который хранит кортежи из индексов смежной веришины и весами ребер
    csv_creator(adjacency_list,Matrix_oriented)
    print("Adjlist: ",adjacency_list)
    print("actual middle degree: ", result_middle_degreee)

elif question==2:## неориентированный
    for i in range(len(Matrix_not_oriented)):## заполнение матрицы числами из метода
        for j in range(random.randint(0, middle_degree), middle_degree, 1):
            Matrix_not_oriented[i][j] = random.randint(0, middle_degree**2)

    for i in range (len(Matrix_not_oriented)):
        for j in range(len(Matrix_not_oriented)):
            Matrix_not_oriented[i][j] = Matrix_not_oriented[j][i]  ##соблюдение условия симметричности
            Matrix_not_oriented[i][i] = 0##заполение нулями главной диагонали
    for i in range (len(Matrix_not_oriented)):
        print(Matrix_not_oriented[i])
    #print("Matrix: ",Matrix_not_oriented)
    degree_counter(Matrix_not_oriented)
    result_middle_degree = sum(count_list) / size_matrix## фактическая средняя степень вершин
    ##создание списка смежности

    adjacency_list_simple = [[j for j in range(len(Matrix_not_oriented[i])) if Matrix_not_oriented[i][j] != 0] for i in
                      range(len(Matrix_not_oriented))]
    csv_creator(adjacency_list_simple, Matrix_not_oriented)

    adjacency_list = []
    for i in range(size_matrix):
        adjacency_list.append([])
    for i in range (len(Matrix_not_oriented)):
        for j in range(len(Matrix_not_oriented)):
            if Matrix_not_oriented[i][j] != 0:
                list_temp = (j,Matrix_not_oriented[i][j])
                adjacency_list[i].append(list_temp[0])
                adjacency_list[i].append(list_temp[1])

    csv_creator(adjacency_list,Matrix_not_oriented)
    ##создание csv файла и помещение туда списка смежности
    print("Adjlist: ",adjacency_list)
    print("actual middle degree:",result_middle_degree)
else:
    print("incorrect data")
time = time.time() - start_time
print('running time program is ->', round(time, 4), '<- seconds')