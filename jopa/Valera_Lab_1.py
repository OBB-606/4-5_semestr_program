import csv
import random
import math

from numpy.random import poisson

Matrix_not_oriented = []
Matrix_oriented = []
count_list = []
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
    with open("adj_list_lab_1.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for i in range(len(Matrix)):
            writer.writerow(adj_list[i])

print("Oriented(1) / not oriented(2)")
question = int(input())
middle_degree = int(input("Write middle degree: "))
if question==1:## ориентированный
    for i in range(len(Matrix_oriented)):
        for j in range(poisson(middle_degree)):
            Matrix_oriented[i][j] = poisson(middle_degree)


    for i in range(len(Matrix_oriented)-1):#соблюдение условия ориентированности, путем целенаправленного
        ##несимметризирования матрицы
        Matrix_oriented[i] = Matrix_oriented[i+1]

    for i in range(len(Matrix_oriented)):
        for j in range(len(Matrix_oriented)):
            Matrix_oriented[i][i] = 0##заполнение нулями главной диагонали

    degree_counter(Matrix_oriented)
    print(Matrix_oriented)
    result_middle_degreee = sum(count_list)/ size_matrix
    adjacency_list = [[j for j in range(len(Matrix_oriented[i])) if Matrix_oriented[i][j] !=0]for i in range(len(Matrix_oriented))]
    csv_creator(adjacency_list,Matrix_oriented)
    print("Adjlist: ",adjacency_list)
    print("actual middle degree: ", result_middle_degreee)

elif question==2:## неориентированный
    for i in range(len(Matrix_not_oriented)):## заполнение матрицы числами из метода
        for j in range(poisson(middle_degree)):
            Matrix_not_oriented[i][j] = poisson(middle_degree)

    for i in range (len(Matrix_not_oriented)):
        for j in range(len(Matrix_not_oriented)):
            Matrix_not_oriented[i][i]=0##заполение нулями главной диагонали
            Matrix_not_oriented[i][j] = Matrix_not_oriented[j][i]##соблюдение условия симметричности

    print("Matrix: ", Matrix_not_oriented)
    degree_counter(Matrix_not_oriented)
    result_middle_degree = sum(count_list)/ size_matrix## фактическая средняя степень вершин
    ##создание списка смежности
    adjacency_list = [[j for j in range(len(Matrix_not_oriented[i])) if Matrix_not_oriented[i][j] !=0]for i in range(len(Matrix_not_oriented))]
    csv_creator(adjacency_list,Matrix_not_oriented)
    ##создание csv файла и помещение туда списка смежности
    print("Adjlist: ",adjacency_list)
    print("actual middle degree:",result_middle_degree)
else:
    print("incorrect data")





