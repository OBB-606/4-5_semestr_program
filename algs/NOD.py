a = int(input("a = "))
b = int(input("b = "))
min = 0
NOD = 0

if a == b:
    NOD = a
else:
    if a > b:
        min = b
    else:
        min = a
    NOD = min

    while a % NOD != 0 or b % NOD != 0:
        NOD -= 1
print(NOD)

# NOD по Евклиду

a = int(input("a = "))
b = int(input("b = "))

while a != b:
    if a > b:
        a -= b
    else:
        b -= a
NOD = a
print(NOD)
