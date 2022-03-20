import random
import csv

def generate_list(size):
    adj_list = []
    part1 = set()
    for i in range(size//2):
        part1.add(i)
    part2 = set()
    for i in range(size // 2, 2*(size//2)):
        part2.add(i)
    for i in range(size//2):
        adj = [[x] for x in list(part2)]
        for j in range(len(adj)):
            adj[j].append(random.randint(10, 90))
        adj_list.append(adj)
    for i in range(size//2, size):
        adj = [[x] for x in list(part1)]
        for j in range(len(adj)):
            adj[j].append(random.randint(10, 90))
        adj_list.append(adj)
    for i in range(len(adj_list)):
        print(adj_list[i])
    return adj_list

def csv_creator(adj_list:list):##метод созданиет csv файл и записывает в него список смежности
    with open("adj_list_for_6_hungarian_small.csv", "w", newline="",) as csvfile:
        writer = csv.writer(csvfile, delimiter = ';', quoting = csv.QUOTE_NONE)
        for i in range(len(adj_list)):
            writer.writerow(adj_list[i])

size = int(input("write size:"))
adj_list = generate_list(size)
csv_creator(adj_list)