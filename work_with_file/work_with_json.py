import json
import csv
import random

first_dict = dict()

for i in range(18):
    first_dict[int(i)] = random.randint(i, 18) + random.randint(0, 9999) * 2

print(first_dict)

with open("testing.json", "w") as json_file:
    json.dump(first_dict, json_file, indent=4)

with open("testing.json", "r") as json_file:
    dict_from_json = json.load(json_file)

print(dict_from_json)