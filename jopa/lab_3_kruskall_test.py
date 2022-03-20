import csv

#Из csv файла извлекается список смежности и преобразовывается в кортеж,
# где (вес ребра, смежная вершина_1, смежная вершина_2).
# .
with open ("adj_list_lab_1_for_3_new_type.csv", mode = 'r', encoding = "utf-8")as r_file:
    file_reader = csv.reader(r_file,delimiter =";",quoting=csv.QUOTE_MINIMAL)
    Adj_list = []
    for row in file_reader:
        Adj_list.append(row)

size = len(Adj_list)
Adj_list_final = [[int(j) for j in i]for i in Adj_list]
Adj_list_tuples = []

for i in range(len(Adj_list_final)):
    for j in range(0, len(Adj_list_final[i]) - 1, 2):
        temp_tuple = (Adj_list_final[i][j+1], i, Adj_list_final[i][j])
        Adj_list_tuples.append(temp_tuple)

main_list = []

for i in range(len(Adj_list_tuples)):
    main_list.append(Adj_list_tuples[i])

#main_list = [( 13 , 1 , 2 ), ( 18 , 1 , 3 ), ( 17 , 1 , 4 ), ( 14 , 1 , 5 ), ( 22 , 1 , 6 ),
     #( 26 , 2 , 3 ), ( 22 , 2 , 5 ), ( 3 , 3 , 4 ), ( 19 , 4 , 6 )]
#ожидаемый вывод при хардкоде: [(3, 3, 4), (13, 1, 2), (14, 1, 5), (19, 4, 6), (17, 1, 4)]

list_of_edges_sorted = sorted(main_list, key = lambda weight:weight[0])#сортировка по весу ребер (по возрастанию)
list_connected_vertices = set()#список уже соединенных вершин (хотя бы одним ребром)
list_isolated_vertices_group = {}#словарь списка изолированных групп вершин (для определения: какая вершина к какой группе относится)
minimum_spanning_tree = []#минимальное остовное дерево

def csv_creator_1(adj_list:list):##метод созданиет csv файл и записывает в него список смежности
    with open("adj_list_lab_3_for_min_span_tree", "w", newline="",) as csvfile:
        writer = csv.writer(csvfile, delimiter = ';')
        for i in range(len(adj_list)):
            writer.writerow(adj_list[i])

for vertex in list_of_edges_sorted:#первая итерация алгоритма, в котором соединяются вершины из разных групп (соед)

    if vertex[1] not in list_connected_vertices or vertex[2] not in list_connected_vertices:#проверка на ацикличность , если одна из вершин не входит в множество соединенных вершин, значит, она изолирована.
        if vertex[1] not in list_connected_vertices and vertex[2] not in list_connected_vertices:#если обе вершины не входят в множество, то они обе изолированы и надо их соединить ребром минимльного веса
            list_isolated_vertices_group[vertex[1]] = [vertex[1], vertex[2]]#формируем словарь, который содержит список соединенной группы вершин, ключами
            #этого словаря будут являться номера этих вершин .
            list_isolated_vertices_group[vertex[2]] = list_isolated_vertices_group[vertex[1]]#словарь на основе второй вершины, и он тоже ссылается на список соединенной группы вершин
        else:

            if not list_isolated_vertices_group.get(vertex[1]):#если в словаре нет первой вершины
                list_isolated_vertices_group[vertex[2]].append(vertex[1])#добавляем в список ту вершину, которая была изолирована
                list_isolated_vertices_group[vertex[1]] = list_isolated_vertices_group[vertex[2]]#добавляем ключ с номером первой вершины

            else:
                list_isolated_vertices_group[vertex[1]].append(vertex[2])#то же самое, только для второй вершины, если она была изолирована
                list_isolated_vertices_group[vertex[2]] = list_isolated_vertices_group[vertex[1]]

        minimum_spanning_tree.append(vertex)#Добавляем в список остова (ребро, вершина_1, вершина_2)
        list_connected_vertices.add(vertex[1])#добавляем в список соединенных вершин первую вершину (с индексом 1 в кортеже)
        list_connected_vertices.add(vertex[2])#вторую (с индексом 2)

for vertex in list_of_edges_sorted:# вторая итерация алгоритма, в которой соединяются группы соединенных вершин
    if vertex[2] not in list_isolated_vertices_group[vertex[1]] and vertex[1] not in list_isolated_vertices_group[vertex[1]] :#если вершины относится к разным группам соединенных вершин, то надо объединить эти группы ребром минимального веса
        minimum_spanning_tree.append(vertex)#добавление в список остова ребро, соединяющие разные группы вершин
        isolate_group_temp = list_isolated_vertices_group[vertex[1]]
        list_isolated_vertices_group[vertex[1]] += list_isolated_vertices_group[vertex[2]]#соответствующие списки групп вершин объединяем
        list_isolated_vertices_group[vertex[2]] += isolate_group_temp#чтобы разные группы вершин были объединены в один список
print("weigth = vertex_1 <=> vertex_2")
for element in minimum_spanning_tree:#вывод минимального остовного дерева
    print("   ", element[0],"\t\t", element[1], "\t\t\t", element[2])

adj_list_final = []#финальный список смежности
for i in range(size):
    adj_list_final.append([] * size)


for i in range (len(minimum_spanning_tree)):
    temp_value = minimum_spanning_tree [i] [1]
    for j in range (len(minimum_spanning_tree)):
        if temp_value == i:
            adj_list_final[i].append(minimum_spanning_tree [i])
csv_creator_1(adj_list_final)

