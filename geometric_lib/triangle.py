def area(a, h):
    '''
    Вычисляет площадь треугольника.

    Argument:
        a (float): основание треугольника
        h (float): высота, опущенная на основание

    Return:
        float: площадь треугольника

    Пример:
        area(5, 6) = 5 * 6 / 2
    '''
    if not isinstance(a, (int, float)) or not isinstance(h, (int, float)):
        raise TypeError
    return a * h / 2


def perimeter(a, b, c):
    '''
    Вычисляет периметр треугольника.

    Arguments:
        a (float): сторона треугольника
        b (float): сторона треугольника
        c (float): сторона треугольника

    Return:
        float: периметр треугольника

    Пример:
        perimeter(1, 2, 3) = 1 + 2 + 3
    '''
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        raise TypeError
    return a + b + c