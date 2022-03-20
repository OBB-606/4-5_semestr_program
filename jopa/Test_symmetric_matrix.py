import random
size = int(input("Write size matrix: "))
Matrix = []
for i in range(size):
    Matrix.append([0]*size)
for i in range (len(Matrix)):
    for j in range(len(Matrix)):
        Matrix[i][j] = random.randint(0,1)
print(Matrix)
for i in range(len(Matrix)):
    for j in range(len(Matrix)):
        Matrix[i][i] = 0
        Matrix[i][j] = Matrix[j][i]
print(Matrix)
print("------------------------------------------------------------------------------------------------------------------")
Matrix_1 = []
for i in range(size):
    Matrix_1.append([0]*size)
for i in range(len(Matrix_1)):
    for j in range(len(Matrix_1)):
        Matrix_1[i][j] = random.randint(0,1)
for i in range(len(Matrix_1)-1):
    Matrix_1[i] = Matrix_1[i+1]
print(Matrix_1)
for i in range( len(Matrix_1)):
        Matrix_1[i][i] = 0
print(Matrix_1)