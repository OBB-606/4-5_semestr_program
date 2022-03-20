def simple_number(number):
    '''
    Определяет, является ли число простым.
    number - целое положительное число.
    Если простое, то возвращает True, а иначе  - False
    :param number:
    :return:
    '''
    divisor = 2
    while divisor < number:
        if number % divisor == 0:
            return False
        divisor+=1
    return True
print(simple_number(int(input("Write number for simple_number: "))))
def factorize_number(number):
# Раскладывает число на множители. Печатает на их экран. number  - целое положительное число
     divisor = 2
     while number > 1:
         if number % divisor == 0:
             print(divisor)
             number //= divisor
         else:
             divisor += 1
factorize_number(int(input("Write number for factorize: ")))