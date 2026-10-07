import math
from abc import ABC, abstractmethod


# a. Clase base abstracta
class Figura(ABC):
    def __init__(self, color):
        self._color = color

    @abstractmethod
    def obtenerArea(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__} de color {self._color} - Área: {self.obtenerArea():.2f}"


class Cuadrado(Figura):
    def __init__(self, color, lado):
        super().__init__(color)
        self.__lado = lado

    # b. Sobrescribir obtenerArea()
    def obtenerArea(self):
        return self.__lado ** 2


class Triangulo(Figura):
    def __init__(self, color, lado1, lado2, lado3):
        super().__init__(color)
        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__lado3 = lado3

    # b. Sobrescribir obtenerArea() (fórmula de Herón)
    def obtenerArea(self):
        s = (self.__lado1 + self.__lado2 + self.__lado3) / 2
        return math.sqrt(s * (s - self.__lado1) * (s - self.__lado2) * (s - self.__lado3))


class Redondo(Figura):
    def __init__(self, color, radio):
        super().__init__(color)
        self.__radio = radio

    # b. Sobrescribir obtenerArea()
    def obtenerArea(self):
        return math.pi * self.__radio ** 2


# d. Dado un Cuadrado y un Triángulo, devolver el color de la figura con mayor área
def color_de_mayor_area(cuadrado, triangulo):
    if cuadrado.obtenerArea() > triangulo.obtenerArea():
        return cuadrado._color
    return triangulo._color


def main():
    # c. Instanciar 2 objetos de cada subclase y mostrarlos
    cuadrado1 = Cuadrado("rojo", 4)
    cuadrado2 = Cuadrado("azul", 6)
    triangulo1 = Triangulo("verde", 3, 4, 5)
    triangulo2 = Triangulo("amarillo", 6, 8, 10)
    redondo1 = Redondo("negro", 2)
    redondo2 = Redondo("blanco", 5)

    figuras = [cuadrado1, cuadrado2, triangulo1, triangulo2, redondo1, redondo2]

    print("=== Figuras creadas ===")
    for figura in figuras:
        print(figura)

    # d. Comparar un Cuadrado y un Triángulo
    print("\n=== Figura con mayor área (Cuadrado 1 vs Triángulo 1) ===")
    print("Color:", color_de_mayor_area(cuadrado1, triangulo1))


if __name__ == "__main__":
    main()