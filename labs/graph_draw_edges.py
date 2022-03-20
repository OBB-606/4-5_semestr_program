import math
import csv

class Node:
    def __init__(self, id, neighborlist):
        self.id:int = id
        self.neighbors = tuple(neighborlist)
        self.busy_colors = []
    def print_me(self):
        print(f"id: {self.id}, connects: {self.neighbors}")

def print_result(colors_max, colors, len):
    print(f"\nХроматическое число для данного графа: {colors_max}")
    print("\nЦвета вершин:")
    for i in range(len):
        print(f"{i+1} - color #{colors[i]}")

def pow_sort(powers): # сортирует вершины по их степени от наиболее часто встречаемой к наименее
    list_ = list(powers.items())
    list_.sort(reverse=True, key=lambda i: i[1])
    list_ = list(i for i, j in list_)
    return list_

def refactor(q, size):
    V = []
    for i in range(size):
        nblist = []
        for j in range(size):
            if int(q[i][j])!=0:
                nblist.append(j)
        V.append(Node(i, nblist))
    return V

def search_neighbors(g, index, painted): # возвращает -1, если не нашлось цвета, с вершинами которого нет смежности
    cid = 0
    for i in painted:
        z = 1
        for j in i:
            if g[j][index]==1: z = 0
        if z==1: return cid+1
        cid+=1
    return -1

def painting_vertices(V, sorted, edges):
    maxcolor = 0
    #print(sorted)
    while len(sorted)>0:
        thisV = sorted.pop(0)
        for j in V[thisV].neighbors:
            if edges[thisV][j]==-1:
                for k in range(0, maxcolor+1):
                    if k not in V[thisV].busy_colors and k not in V[j].busy_colors:
                        V[thisV].busy_colors.append(k)
                        V[j].busy_colors.append(k)
                        edges[thisV][j] = k
                        edges[j][thisV] = k
                        break
                if edges[thisV][j] == -1:
                    maxcolor +=1
                    V[thisV].busy_colors.append(maxcolor)
                    V[j].busy_colors.append(maxcolor)
                    edges[thisV][j] = maxcolor
                    edges[j][thisV] = maxcolor
    print("Матрица раскраски рёбер по цветам:")
    for i in edges:
        for j in i:
            if j==-1: print("-", end='\t')
            else: print(f"{j}", end = '\t')
        print()
    print(f"Хроматический индекс: {maxcolor+1}")

def painting(q, sorted):
    n = len(q)
    colors = [0]*n
    colors[sorted[0]] = 1
    colors_max = 1
    painted = [[sorted[0]]]

    for i in range(1, n):
        f = sorted[i]
        cid = search_neighbors(q, f, painted) # если cid == -1, т.е. "свободных" цветов нет, вводим новый цвет, иначе присваиваем существующий
        if cid == -1:
            colors_max+=1
            r = [f]
            painted.append(r)
            colors[f] = colors_max
        else:
            painted[cid-1].append(f)
            colors[f] = cid

    print_result(colors_max, colors, len(q))

if __name__ == '__main__':
    q = [[0, 1, 0, 0, 0, 1, 0, 1],
         [1, 0, 1, 0, 1, 0, 0, 1],
         [0, 1, 0, 1, 0, 0, 0, 1],
         [0, 0, 1, 0, 1, 0, 1, 0],
         [0, 1, 0, 1, 0, 1, 1, 0],
         [1, 0, 0, 0, 1, 0, 1, 0],
         [0, 0, 0, 1, 1, 1, 0, 1],
         [1, 1, 1, 0, 0, 0, 1, 0]
    ]
    # if input("1 - открыть файл со списком смежности, 0 - сгенерировать новый список: ")=='0':
    #     q = generator(True)
    # else:
    #     project_name = input("Название файла для открытия: ")
    #     with open(f"graphs\\{project_name}.csv", mode="r", newline='\r\n', encoding='utf-8') as file:
    #         fileread = csv.reader(file, delimiter=',')
    #         q=[]
    #         for str in file:
    #             f = str.split(',')
    #             f[-1] = f[-1].split('\r')[0]
    #             if not(len(f)==1): q.append(f)
    #     #print(q)
    #     print(q)

    size = len(q)
    edges = [[-1]*size for i in range(size)]
    powers = {}
    for i in range(size):
        pow = 0
        for j in range(size):
            if q[i][j]!=0: pow+=1
        powers[i] = pow

    #print(powers)
    sorted = pow_sort(powers)
    V = refactor(q, size)
    painting_vertices(V, sorted, edges)