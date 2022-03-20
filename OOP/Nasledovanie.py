
class Jopa:
    __List = []
    def __init__(self):
        self.__List = Jopa.__List
    @property
    def List(self):
        return self.__List
    @List.setter
    def List(self, value):
        self.__List.append(value)
class Rock:
    x = Jopa()
    x.List = 2
    print(x.List)

