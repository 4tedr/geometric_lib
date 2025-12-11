import math


def area(r):
    '''
    Вычисляет площадь круга.

    Argument:
        r (float): радиус круга

    Return:
        float: площадь круга

    Пример:
        area(4) = math.pi * 4 * 4
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Вычисляет длину окружности.

    Arguments:
        r (float): радиус круга

    Return:
        float: длина окружности

    Пример:
        perimeter(3) = 2 * math.pi * 3
    '''
    return 2 * math.pi * r

