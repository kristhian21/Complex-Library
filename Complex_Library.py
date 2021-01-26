import math


def sumaComplejos(c1, c2):
    return c1[0] + c2[0], c1[1] + c2[1]


def restaComplejos(c1, c2):
    return c1[0] - c2[0], c1[1] - c2[1]


def divisionComplejos(c1, c2):
    return c1[0] * c2[0] + c1[1] * c2[1] + c2[0] * c1[1] - c1[0] * c2[1]


def productoComplejos(c1, c2):
    a = (c1[0] * c2[0]) + (-(c1[1] * c2[1]))
    b = (c1[0] * c2[1]) + (c1[1] * c2[0])

    return a, b


def moduloComplejos(c):
    m = math.sqrt((c[0])** 2 + (c[1])** 2)

    return round(m, 3)


def conjugadoComplejos(c):
    return c[0], -c[1]


def cartesiano_polar(c):
    p = moduloComplejos(c)
    g = faseComplejos(c)

    return round(p, 3), g


def polar_cartesiano(polar):
    a = polar[0] * math.cos(math.radians(polar[1]))
    b = polar[0] * math.sin(math.radians(polar[1]))

    return round(a, 3), round(b, 3)


def faseComplejos(c):
    fase = math.degrees(math.atan(c[1] / c[0]))

    if c[0] < 0 and c[1] < 0:
        fase = 180 + fase
        return round(fase, 3)

    elif c[1] < 0 < c[0]:
        fase = 270 + fase 
        return round(fase, 3)

    elif c[0] < 0 < c[1]:
        fase = 90 + fase 
        return round(fase, 3)

    elif c[0] > 0 and c[1] > 0:
        return round(fase, 3) 




def main():
    pass

if __name__ == '__main__':
    main()
