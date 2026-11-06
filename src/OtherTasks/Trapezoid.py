from math import sqrt

class Trapezoid:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def check(self):
        if self.a == self.c:
            print("Трапеция является равнобокой))")
        else:
            print("Трапеция НЕ РАВНОБОКАЯ((")

    def info_sides(self):
        print(f"Левая сторона a = {self.a}\n"
              f"Верхняя сторона b = {self.b}\n"
              f"Правая сторона c = {self.c}\n"
              f"Нижняя сторона d = {self.d}")

    def perimetr(self):
        print(f"Периметр трапеции = {self.a + self.b + self.c + self.d}")

    def square(self):
        print(f"Площадь трапеции = {((self.b + self.d)*self.__height())/2:.0f}")

    def __height(self): #Написано что так помечаются private методы (потому что модификаторов доступа в питоне нет)
        return sqrt(self.a**2-(((self.d-self.b)**2 + self.a**2 - self.c**2)/(2*(self.d-self.b)))**2)


kakaytoTrapezoid = Trapezoid(4,5,3,10)
kakaytoTrapezoid.info_sides()
kakaytoTrapezoid.check()
kakaytoTrapezoid.perimetr()
kakaytoTrapezoid.square()

print()

second_trapezoid = Trapezoid(5,8,5,14)
second_trapezoid.info_sides()
second_trapezoid.check()
second_trapezoid.perimetr()
second_trapezoid.square()