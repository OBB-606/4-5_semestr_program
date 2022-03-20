import math
import random
def get_position(labda):
    l = math.exp(-labda)
    p = 1.0
    k = int(0)
    while p > l or k == 0:
        k += 1
        p *= random.random()
    return k - 1

degree = int(input("write degree: "))
size = int(input("write size matrix: "))
Matrix =[]
for i in range(size):
    Matrix.append([0]*size)
for i in range(len(Matrix)):
    for j in range(len(Matrix)):
        Matrix[i][j] = random.randint(0,1)
print(Matrix)
for i in range(len(Matrix)):
    for j in range (len(Matrix)):
        Matrix[i][j] = get_position(degree)
for i in range(len(Matrix)):
    for j in range(len(Matrix)):
        Matrix[i][i] =0
        Matrix[i][j] = Matrix[j][i]
print(Matrix)
count_array = []
for i in range(len(Matrix)):
    count = int(0)
    for j in range (len(Matrix)):
        if Matrix[i][j] != 0:
            count+=1
    count_array.append(count)
result_middle_degree =  sum(count_array) / size
print(count_array, result_middle_degree)