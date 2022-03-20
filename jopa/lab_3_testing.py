import sys
import random
from numpy.random import poisson
middle_degree = int(input("write middle degree:"))
infinity = sys.maxsize
Matrix  = []
for i in range(10):
    Matrix.append([0]*10)
for i in range(random.randint(0,middle_degree), len(Matrix), 1):
    for j in range(random.randint(0, middle_degree), middle_degree, 1):
        Matrix[i][j] = poisson(middle_degree)
for i in range(len(Matrix)):
    for j in range(len(Matrix)):
        Matrix[i][j] = Matrix [j][i]
        Matrix[j][j] = 0
for i in range(len(Matrix)):
    print(Matrix[i],"\n")
adj_list = [[j for j in range(len(Matrix[i])) if Matrix[i][j] != 0]for i in range(len(Matrix))]
for i in range(len(adj_list)):
    print("\n",adj_list[i])
