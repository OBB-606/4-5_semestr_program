import csv
import random

with open("adj_list_lab_4_nice_1.csv", encoding = "utf-8") as r_file:
    file_reader = csv.reader(r_file)
    Adj_list = []
    count_vertex = 0
    for row in file_reader:
        count_vertex += 1
        Adj_list.append(row)

Adj_list_int = [[int(j) for j in i] for i in Adj_list]
one_prozent = count_vertex / 100
visited = []
vertex = random.randint(0, count_vertex)
list_counter = []
counter = 0
vertex_temp = 0
print("---------------")

def dfs(graph, vertex, flag = 0): #поиск в глубину
    counter = 0
    global visited
    visited.append(vertex)
    to_explore = [vertex]
    while to_explore:# пока стек не пуст
        current = to_explore.pop()# извлечение и удаление из стека
        counter += 1
        vertex_temp = vertex
        print("dfs: ", current)
        new_vertices = [i for i in graph[current] if i not in visited]  # graph[u]- список из смежных вершин в списке смежности z.B [1,2,3]
        # если вершина из этого списка еще не посещена, то она помещается в список new_vertices
        to_explore.extend(new_vertices)  # очередь дополняется списком new_vertices(непосещенными вершинами)
        visited.extend(new_vertices)# множество посещенных вершин тоже дополняется этим списком(посещенными вершинами)
    temp_tuple = (counter, vertex_temp)
    list_counter.append(temp_tuple)

    if (len(visited) < count_vertex) and flag == 0:
        print("-----------", len(visited) / one_prozent, "%", "----------")
        for i in range(count_vertex):
            if i not in visited:
                temp = i
        dfs(Adj_list_int, temp)#рекурсивный вызов метода для полного обхождения графа в случае наличия в нем нескольких компонент связности
    elif flag == 1:
        print("-----------", int(len(visited) / one_prozent), "----------")
    else:
        print("Граф был полностью обойден")

dfs(Adj_list_int, vertex)
print(list_counter)
print("Количество связных компонент: ", len(list_counter))
max = list_counter[0][0]
i_temp = 0
visited.clear()
for i in range(len(list_counter)):#поиск вершины с которой начинался обход, если начать обход с этой вершины, то будет выявлена макс.связ.компонента
    if list_counter[i][0] >= max:
        max = list_counter[i][0]
        max_1 = list_counter[i]

print("Максимальная связная компонента: ")
dfs(Adj_list_int, max_1[1], flag = 1)