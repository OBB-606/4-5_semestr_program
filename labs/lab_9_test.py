import csv
import time as t

time_start = t.time()

with open("adj_list_lab_1_for_3_new_type.csv", mode = 'r', encoding = "utf-8")as r_file:
    file_reader = csv.reader(r_file, delimiter =",", quoting=csv.QUOTE_MINIMAL)
    Adj_list = []
    for row in file_reader:
        Adj_list.append(row)
size = len(Adj_list)
graph = [[int(j) for j in i]for i in Adj_list]

#print(graph)

def coloring (graph, vertices):#метод раскраски, в который передается список смежности и список вершин.
    colors = dict()#Словарь, где будут находиться цвета
    for v in vertices:
        min_color = set(vertices)#в переменной min_color хранится множество доступных для раскраски вершины v цветов
        for u in graph[v]:
            if u in colors:#выполняется првоерка : раскрашена вершина или нет
                min_color.discard(colors[u])#если эта вершина u есть в словаре colors, то соответствующий элемент(цвет)
                # убирается из множества min_color
        colors[v] = min(min_color)#раскраска вершины
    return colors

vertices = list(range(len(graph)))
#print(coloring(graph, vertices))
result = coloring(graph, vertices)
print("vertex\t\tcolor")
temp = result[0]
for i in range(0, len(result), 1):
    print("\t", i, "\t\t", result[i])
    if temp < result[i]:
        temp = result[i]
print("Хроматическое число = ", temp)
count_list = dict()
def degree_counter(Matrix:list, count_list:dict):## метод ищет степень связности каждой вершины графа
    for i in range(len(Matrix)):
        count = 0
        for j in range(len(Matrix[i])):
            if Matrix[i][j] >= 0:           # >= так как adj_list
                count += 1
        count_list[i] = count
degree_counter(graph, count_list)

print("максимальная степень связности = ", max(count_list))
print("средняя степень связности = ", sum(count_list)/len(graph))



def coloring_edges(graph:list, list_degree_of_connectivity:dict):
    degree_counter(graph, list_degree_of_connectivity)
    color_edges = dict()


list_degree_of_connectivity = dict()
coloring_edges(graph, list_degree_of_connectivity)
print("vertex\t\tdegree of connectivity")
for i in range(len(graph)):
    print(i, "\t\t\t", list_degree_of_connectivity[i])



time_running_program = t.time() - time_start
print("program running time is ", round(time_running_program, 4), "seconds")

