class Point:
    "геттеры сеттеры"
    def __init__(self, x , y):
        self.__x = x
        self.__y = y
    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x_y(self, x, y):
        self.__x = x
        self.__y = y
    def get_all_coords(self):#возвращение из геттера атрибутов в виде кортежа
        return self.__x, self.__y

pt = Point(1,2)
print(pt.get_x())
print(pt.get_y())

x = int(input("write x for update value: "))
y = int(input("write y for update value: "))

pt.set_x_y(x, y)
print(pt.get_x())
print(pt.get_y())
tuple = pt.get_all_coords()
print(tuple[0])