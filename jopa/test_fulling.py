import random as rd
from numpy.random import poisson
middle_degree = int(input("write the middle degree: "))
list = []
for i in range (20):
    list.append([0]*20)
temp = range(0,20)

for i in range(middle_degree):
    for j in range(len(list)):
        list[j][i] = rd.randint(0,1)

for i in range(len(list)):
    for j in range(len(list[i])):
        list[j][i] = list[i][j]
        list[j][j] = 0

adj_list =[[j for j in range(len(list)) if list[i][j]!=0] for i in range(len(list))]



for i in range(len(list)):
    print(list[i])

for i in range(len(adj_list)):
    print("\n",adj_list[i])
