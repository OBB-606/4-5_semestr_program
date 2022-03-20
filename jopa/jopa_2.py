import random
import pandas



Matrix_not_oriented = []
for i in range (4):
    Matrix_not_oriented.append([0]*4)

for i in range(4):
    for j in range (4):
        Matrix_not_oriented[i][j] = random.randint(0,9)

for i in range(len(Matrix_not_oriented)-1):
    Matrix_not_oriented [i] = Matrix_not_oriented [i+1]
for i in range (len(Matrix_not_oriented)):
    Matrix_not_oriented[i][i] = 0
adj_list_final = []

for i in range(4):
    adj_list_final.append([])

for i in range(len(Matrix_not_oriented)):
    for j in range (len(Matrix_not_oriented)):
        if Matrix_not_oriented[i][j] != 0:
            list_temp = (j,Matrix_not_oriented[i][j])
            adj_list_final[i].append(list_temp)

for i in range (len(Matrix_not_oriented)):
    print(Matrix_not_oriented[i])
print("\n")

for i in range (len(adj_list_final)):
    print(adj_list_final[i])


df = pandas.read_csv('adj_list_lab_1_for_3.csv', index_col=0)
print("\n",df)