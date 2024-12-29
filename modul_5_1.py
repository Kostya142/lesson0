class House:   # От этой строки блока кода и вниз - три ДЗ по теме "классы"
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors =number_of_floors
    def go_to(self,new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print(f'"{new_floor}"___"Такого этажа не существует"')
        else:
            for i in range(new_floor+1):
                print(i)
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f'{self.name},кол-во этажей:{self.number_of_floors}'
    def __eq__(self, other):
        # if isinstance(other, int):
            return self.number_of_floors == other
        # else:
        #     return self.number_of_floors == other.number_of_floors
    def __add__(self, other):
            return self.number_of_floors + other
    def __iadd__(self):
        return self.number_of_floors
    def __radd__(self, other):
        return self.number_of_floors + other
    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors
    def  __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors
    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors
    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors
D_1 = House('ЖК Сити',11)
D_2 = House('ЖК Уют', 3)
D_1.go_to(4)
print()
D_2.go_to(4) # конечная строка кода ДЗ по уроку "Атрибуты и методы объекта"
print('*******')
print(len(D_1))
print(len(D_2))
print(str(D_1))
print(str(D_2)) # конечная строка кода ДЗ по уроку "Специальные методы классов"
print('*******')
print(D_1)
print(D_2)
print(D_1 == D_2) #__eq__
D_2 = D_2 + 8    #__add__
print(D_2)
print(D_1 == D_2)
D_2+=8          # __iadd__
print(D_2)
D_1=8+D_1        # __radd__
print(D_1)
print(D_2>D_1)   # __gt__
print(D_2>=D_1)  #__ge__
print(D_2<D_1)   #__lt__
print(D_2<=D_1)   #__le__
print(D_2!=D_1)   #__ne__ 'Конечная строка кода ДЗ по уроку "Перегрузка операторов"



