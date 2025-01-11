class House:   # От этой строки блока кода и вниз -  ДЗ по теме Различие атрибутов класса и экземпляра
    houses_history = []
    def __new__(cls, *args, **kwargs):
        name = args[0]
        cls.houses_history.append(name)
        return super().__new__(cls)
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors =number_of_floors
    def __del__(self):
        print(self.name, 'снесён,но останется в летописи.')

H_1 = House('ЖК Сити',11)
print(House.houses_history)
H_2 = House('ЖК Уют', 3)
print(House.houses_history)
H_3 = House('ЖК Парк', 2)
print(House.houses_history)
H_4 = House('ЖК Башня',12)
print(House.houses_history) #Выводим названия созданных объектов
del H_2
del H_4
print(House.houses_history)
print("--------")