import random

password = 12345678910
size_password = len(str(password))
print(size_password*10)

password_array = [password // 1 % 10, password // 10 % 10, password // 100 % 10, password // 1000 % 10, password // 10000 % 10]
password_array.reverse()
print(password_array)

while(True):
    #password_temp = int(input('write the password: '))
    password_temp = 0
    if password == password_temp:
        break
    else:
        password_array_temp = [] * len(password_array)
        for i in range(len(password_array)):
            for j in range(10):
                if j == password_array[i]:
                    password_array_temp.append(j)
        print(password_array_temp)
        break
print(password // 1 % 10 )



