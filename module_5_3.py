class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        int(new_floor)
        for i in range(1, new_floor+1):
            if new_floor > self.number_of_floors:
                print('Такого этажа не существует')
                break
            else:
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, количество этажей: {self.number_of_floors}"

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        self.number_of_floors = self.number_of_floors + value
        return self

    def __iadd__(self, value):
        self.number_of_floors = self.number_of_floors + value
        return self

    def __radd__(self, value):
        self.number_of_floors = self.number_of_floors + value
        return self


h1 = House('ЖК Солнечный', 12)
h2 = House('Хижина люкс', 3)
#h1.go_to(13)
#h2.go_to(2)
print(h1)
print(h2)
#print(len(h1))
#print(len(h2))
print(h1 == h2)
h2 = h2 + 9
print(h2)
print(h1 == h2)
h2 += 10
h1 = 10 + h1
print(h1)
print(h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 > h2)
print(h1 >= h2)
print(h1 != h2)








