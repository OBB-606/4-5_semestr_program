import networkx as nx
import random
import math
import matplotlib.pyplot as plt
import numpy as np

g = nx.DiGraph()
N = 1000
A = [i for i in range(N)]
B = []
C = []
massiv = []
for i in range(N):
    massiv.append([])
G = list(range(N))
while len(C) != N:
    r = random.choice(G)
    if r not in C:
        count = 0
        while count !=3:
            if len(A) != 0:
                r2 = random.choice(A)
            else:
                r2 = random.choice(G)
            if r2 != r and r2 not in B:
                massiv[r].append(r2)
                g.add_edge(r, r2)
                B.append(r2)
                count += 1
                if r2 in A:
                    A.remove(r2)
        C.append(r)
        B.clear()

vector = []
line = 1
count = 0
for i in range(len(massiv)):
    if count == 14:
        vector.append(round(line, 3))
    else:
        qq = round(random.uniform(0, line), 3)
        line = line - qq
        vector.append(qq)
        count += 1
print("Вектор начальных вероятностей:")
print(vector)
print('Сумма начальных вероятностей:',sum(vector))
matrix = []
for i in range(N):
    matrix.append([])
    k = 0
    while k < N:
        matrix[i].append(0)
        k += 1
for i in range(len(massiv)):
    line = 1
    count = 0
    for j in range(len(massiv[i])):
        if count == 2:
            matrix[i][int(massiv[i][j])] = round(line,3)
        else:
            qq = round(random.uniform(0,line),3)
            line = line - qq
            matrix[i][int(massiv[i][j])] = qq
            count += 1
print("Матрица переходов:")
for i in range(len(matrix)):
    print(matrix[i])
nx.draw(g, with_labels=True)
plt.show()

a = 0

ver = []
for i in range(len(matrix)):
    ver.append([])
j = len(matrix)-1
k = 0
while k != len(matrix)-1:
    for i in range(len(matrix)):
        ver[k].append(matrix[i][j])
    sum = 0
    for i in range(len(matrix)):
        sum += matrix[j][i]
    ver[k][j] = -sum
    k +=1
    j -= 1
for i in range(len(matrix)):
    ver[k].append(1)
v = []
for i in range(len(matrix)-1):
    v.append(0)
v.append(1)
print("Предельные вероятности системы: ")
kk = np.linalg.solve(ver, v)
for i in range(len(kk)):
    print("p%d" % int(i+1), kk[i])
k = int(input("Шаг: "))
s = int(input("Откуда: "))
t = int(input("Куда: "))
vector1 = []
for i in range(N):
    vector1.append(matrix[s-1][i])
count = 0
while count < k-1:
    for i in range(N):
        aa = 0
        for j in range(N):
            aa += vector1[j] * matrix[j][i]
        vector1.append(aa)
    for i in range(N):
        vector1.pop(0)
    count += 1
print("вероятность пребывания пакета в узле j после k коммутаций при условии, что пакет поступил в сеть через узел i: ", round(vector1[t-1],3))#вероятность пребывания пакета в узлах

x = np.linspace(1, N, N)
y1 = vector1
plt.title("Вероятности пребывания пакета в узлах от их номеров")
plt.xlabel("Номер узла")
plt.ylabel("Вероятность")
plt.plot(x, y1,'r*-', color="purple", lw=2, ls='-', marker='s', markersize=8,
        markerfacecolor="red", markeredgewidth=3, markeredgecolor="black")
plt.grid(True)
plt.show()

for i in range(N):
    aa = 0
    for j in range(N):
        aa += vector1[j] * matrix[j][i]
    vector1.append(aa)
for i in range(N):
    vector1.pop(0)
print("вероятность первого перехода пакета в узел j из узла i после k коммутаций: ", round(vector1[t-1],3))#вероятность первого перехода в j из i, после k коммутаций

y1 = vector1
plt.title("Вероятность первого перехода пакета в узел j из узла i после k коммутаций от номеров узлов.")
plt.xlabel("Номер узла")
plt.ylabel("Вероятность")
plt.plot(x, y1, color="green", lw=2, ls='-', marker='o', markersize=8, markerfacecolor="red")
plt.grid(True)
plt.show()

sum = 0
summ = []
j = 0
while len(summ) != N:
    for i in range(k):
        sum += i*math.pow(vector1[j],i)
    summ.append(sum)
    j +=1
    sum = 0
print("Мат ожидание равно: ", round(summ[t-1], 3))#математическое ожидание

y1 = summ
plt.title("Математические ожидания от номеров узлов")
plt.xlabel("Номер узла")
plt.ylabel("Мат ожидание")
plt.plot(x, y1,color="orange", lw=2, ls='-', marker='o', markersize=8, markerfacecolor="green")
plt.grid(True)
plt.show()

sum2 = 0
summ2 = []
j = 0
while len(summ2) != N:
    for i in range(k):
        sum2 += math.pow(i,2)*math.pow(vector1[j],i)
    summ2.append(sum2)
    j += 1
    sum2 = 0
print("Дисперсия равна: ", round(summ2[t-1]-math.pow(summ[t-1],2),3))#дисперсия

y1 = summ2
plt.title("Дисперсия от номеров узлов")
plt.xlabel("Номер узла")
plt.ylabel("Дисперсия")
plt.plot(x, y1, color="blue", lw=2, ls='--', marker='s', markersize=8, markerfacecolor="red")
plt.grid(True)
plt.show()

vector2 = []
for i in range(N):
    vector2.append(matrix[s-1][i])
mink = []
for i in range(N):
    mink.append(0)
count = 1
while 0 in mink:
    for i in range(N):
        if vector2[i] !=0 and mink[i] == 0:
            mink[i] = count
        aa = 0
        for j in range(N):
            aa += vector2[j] * matrix[j][i]
        vector2.append(aa)
    for i in range(N):
        vector2.pop(0)
    count += 1

y1 = mink
plt.title("Длина кратчайших путей переходов от номеров узлов")
plt.xlabel("Номер узла")
plt.ylabel("Кратчайшая длина")
plt.plot(x, y1,color="red", lw=2, ls='-', marker='s', markersize=8, markerfacecolor="yellow")
plt.grid(True)
plt.show()
