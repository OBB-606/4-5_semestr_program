import csv
#Все файлы ty
# раскраска графа
def graphColoring():
    colored = [[]]
    color = 0  # № цвета
    cc = 0
    stack = []  # покрашенные узлы
    num2 = num1 = -1

    # функция проверки возможности покраски в используемый сейчас цвет
    def loop(num):
        for t in colored[color]:
            if g[t][num] == 1:
                return False
        return True

    for a in g:
        num1 += 1
        if num1 not in stack:  # просматриваем только те, которые еще не покрашены
            if not loop(num1):  # значит применяем новый цвет
                colored.append([])
                color += 1
                stack.append(num1)
                colored[color].append(num1)
            num2 = num1
            for b in a[num1:]:
                if b == 0 and num2 not in stack and loop(num2):
                    stack.append(num2)
                    colored[color].append(num2)
                num2 += 1
    return colored

N = int(input("Введите количество вершин: "))
g = []
for i in range(N):
    g.append([])
    k = 0
    while k<N:
        g[i].append(0)
        k += 1
file = input("Введите название файла: ")
T = []
j = 0
with open('{}.csv'.format(file), newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        T.append([])
        d = row
        d = d[0]
        c = 0
        a = ''
        q = ''
        for i in range(len(str(d))):
            if d[i] != ';':
                q = q + d[i]
                if i == len(str(d)) - 1:
                    T[j].append(q)
            else:
                if d[i] == ';':
                    T[j].append(q)
                    q = ''
        j += 1
# print(T)
for k in range(len(T)):
    for h in range(len(T[k])):
        g[k][int(T[k][h])] = 1
# print(g)
color = graphColoring()
for i in range(len(color)):
    print(i+1,"цвет")
    print(color[i])

print("Число различных цветов: ", str(len(color)))
