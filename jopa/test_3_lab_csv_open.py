import csv


size = 100
with open ("adj_list_lab_1_for_3.csv",'r', encoding = "utf-8",)as r_file:
    file_reader = csv.reader(r_file,delimiter =";",quoting=csv.QUOTE_MINIMAL)
    Adj_list = []
    next(file_reader)
    for row in file_reader:
        Adj_list.append(row)
        print(row)
#for i in range(len(Adj_list)):
    #for j in range(len(Adj_list[i])):
        #Adj_list[i][j] = tuple(Adj_list[i][j])
#for i in range(len(Adj_list)):
    #print(Adj_list[i])
str = Adj_list[0][9]
print(str)
str_temp = int(str[1]+str[2])
print(str)

#Adj_list[0][9] = tuple(Adj_list[0][9])
#print(Adj_list[0][9])