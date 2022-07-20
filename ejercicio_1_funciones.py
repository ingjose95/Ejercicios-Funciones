from cmath import pi
import math

def areaTriangulo(base, altura):

    print('El área de un triángulo es: ', (base*altura)/2)


def areaCirculo(radio):

    print('El área de un circulo es: ', round(pi*(radio**radio), 2))

areaTriangulo(10,5)
areaCirculo(2)