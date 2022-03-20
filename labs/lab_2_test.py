import csv
import random

with open("adj_list_lab_1.csv", encoding="utf-8") as r_file:
    file_reader = csv.reader(r_file)
    Adj_list = []
    count_vertex = 0
    for row in file_reader:
        count_vertex += 1
        Adj_list.append(row)

Adj_list_int = [[int(j) for j in i] for i in Adj_list]
one_prozent = count_vertex / 100
print(count_vertex)
list_vertex = list(range(count_vertex))
list_vertex_helper = []
visited = []

def question():
    try:
        global vertex
        vertex = int(input("Вершина, с которой начинается обход: "))
        if vertex < 0 or vertex > count_vertex:
            vertex = int(input("Вершина, с которой начинается обход: "))
            if vertex < 0 or vertex > count_vertex:
                vertex = random.randint(0, count_vertex)
                print("В рез-те неправильного ввода была выбрана рандомная вершина: ")
    except:
        print("Ошибка, введите целое число")
        question()
question()

print("---------------")

def dfs(graph, vertex):  # обход в глубину
    global visited
    visited.append(vertex)
    to_explore = [vertex]
    while to_explore:  # пока стек не пуст
        current = to_explore.pop()  # извлечение и удаление из стека
        print("dfs: ", current)
        new_vertices = [i for i in graph[current] if i not in visited]
        to_explore.extend(new_vertices)  # дополнение стека списком из непосещенных вершин
        visited.extend(new_vertices)  # дополнение множества посещенными вершинами
    if len(visited) < count_vertex:
        print("Граф был обойден не полностью(", "на ", len(visited) / one_prozent, "%)")
        temp = 0
        for i in range(count_vertex):
            if i not in visited:
                temp = i
        dfs(Adj_list_int, temp)
    else:
        print("Граф полностью обойден")

def bfs(graph, vertex):  # поиск в ширину

    global visited
    visited.append(vertex)
    to_explore = [vertex]

    while to_explore:  # пока очередь не пуста
        current = to_explore.pop(0)  # извлечение и удаление из очереди
        print("bfs: ", current)
        new_vertices = [i for i in graph[current] if i not in visited]  # graph[u]- список из смежных вершин в списке смежности z.B [1,2,3]
        # если вершина из этого списка еще не посещена, то она помещается в список new_vertices
        to_explore.extend(new_vertices)  # очередь дополняется списком new_vertices( непосещенными вершинами)
        visited.extend(new_vertices)# множество посещенных вершин тоже дополняется этим списком(посещенными вершинами)

    if len(visited) < count_vertex:
        print("Граф был обойден не полностью(", "на ", len(visited) / one_prozent, "%)")
        temp = 0
        for i in range(count_vertex):
            if i not in visited:
                temp = i
        bfs(Adj_list_int,temp)
    else:
        print("Граф был полностью обойден")

b = int(input("dfs(1)/ BFS(2)"))

if b == 1:
    dfs(Adj_list_int, vertex)
elif b == 2:
    bfs(Adj_list_int, vertex)
else:
    print("incorrect data!")