import random
import csv
import numpy as np

size = int(input("Write size: "))
count = 0
middle_degree = int(input("Write middle degree of vertex: "))
Matrix = [[0] * size for i in range(size)]
for i in range(len(Matrix)):
    for j in range(len(Matrix)):
        Matrix[i][j] = random.randint(0,1)
print(Matrix)
adj_list = [[j for j in range (len(Matrix[i])) if Matrix[i][j]!=0]for i in range (len(Matrix))] # списки смежности
print(adj_list)
with open("lab_1_PI.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    for i in range(len(Matrix)):
        writer.writerow(adj_list[i])
