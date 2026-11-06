import math

class Circle:

    def __init__(self, radius):
        self.radius = radius
        self.area = math.pi * self.radius ** 2

    def increase_radius(self, koef):
        self.radius = self.radius + koef
        self.area = math.pi * self.radius ** 2

    def decrease_radius(self, koef):
        self.radius = self.radius - koef
        self.area = math.pi * self.radius ** 2

    def __eq__(self, other):
        return self.area == other.area

    def __lt__(self, other):
        return self.area < other.area

    def __gt__(self, other):
        return self.area > other.area

circle_1 = Circle(7)
circle_2 = Circle(10)
circle_3 = Circle(9)
circle_4 = Circle(3)
circle_5 = Circle(5)

list_of_circles = [circle_1, circle_2, circle_3, circle_4, circle_5]

print("Изначальный список окружностей")
[print(i.area) for i in list_of_circles]
print()

circle_4.decrease_radius(2)
circle_5.increase_radius(2)

print("Список окружностей после изменения радиусов")
[print(i.area) for i in list_of_circles]
print()

new_list = sorted(list_of_circles)
print("Отсортированный список окружностей")
[print(i.area) for i in new_list]

