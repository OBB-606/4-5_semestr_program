import csv

with open ("adj_list_for_6_hungarian.csv")as r_file:
    file_reader = csv.reader(r_file, delimiter =";")
    Adj_list = []
    for row in file_reader:
        Adj_list.append(row)
size = len(Adj_list)
Adj_list_final = [[j for j in list(i)]for i in Adj_list]

adj_list_global = []

a = Adj_list_final[0][0][2]
print(a)

for i in range(size):
    adj_list_global.append([])



for i in range(len(Adj_list_final)):
    for j in range(len(Adj_list_final[i])):
        first = Adj_list_final[i][j][1]
        second = Adj_list_final[i][j][4]
        try:
            first += Adj_list_final[i][j][2]
            first = int(first)
        except ValueError:
            first = int(Adj_list_final[i][j][1])
        try:
            second += Adj_list_final[i][j][5]
            second = int(second)
            try:
                second = str(second) + Adj_list_final[i][j][6]
                second = int(second)
            except ValueError:
                second = int(Adj_list_final[i][j][5] + Adj_list_final[i][j][6])
        except ValueError:
            second = int(Adj_list_final[i][j][4] + Adj_list_final[i][j][5])
        list_temp = [first, second]
        adj_list_global[i].append(list_temp)

for i in range(len(adj_list_global)):
    print(adj_list_global[i])
