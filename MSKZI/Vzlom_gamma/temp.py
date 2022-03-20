import random
import cowsay
from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ['J', "R", "O"]
limit = 100
for i in range(27):
    table.add_row([random.randint(0, limit), random.randint(0, limit), random.randint(0, limit)])
print(table)