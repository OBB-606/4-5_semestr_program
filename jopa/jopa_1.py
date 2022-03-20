import math
import random
"""
ТОТС 1 лаба
"""


#1)
array_ri =[]

for i in range (200):
    a = random.random()
    array_ri.append(a)

array_ri.sort()
print(array_ri)

#2)
N = 13
lam = 119/N
print(lam)

#3)
array_zi = []

for i in range (200):
    zi = -math.log(1 / lam) * (1-array_ri[i])
    array_zi.append(zi)

array_zi.sort()
print(sum(array_zi))
#count =0

#for i in range(len(array_zi)):
    #if array_zi[i]>=0:
        #count+=1

#print(count)4
#4 and 5)
T1 = N
T2 = N+7
array_tk =[]
tk =0
i=0
count =0
while tk<=T2 or i>=200:
    tk = T1+ array_zi[i]
    i+=1
    count =i
    array_tk.append(tk)
    if tk > T2 or i>=200:
        array_tk.pop()
        break

array_tk.sort(reverse = True)
print(array_tk)
print(count)

#6
tau = (T2 - T1) / 20
print(tau)
