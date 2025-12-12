def area(a, b):
    '''
    Вычисляет площадь прямоугольника.

    Arguments:
        a (float): длина прямоугольника
        b (float): ширина прямоугольника

    Return:
        float: площадь прямоугольника

    Пример:
        area(1, 2) = 1 * 2
    '''
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError
    return a * b


def perimeter(a, b):
    '''
    Вычисляет периметр прямоугольника.

    Arguments:
        a (float): длина прямоугольника
        b (float): ширина прямоугольника

    Return:
        float: периметр прямоугольника

    Пример:
        perimeter(7, 3) = 2 * (7 + 3)
    '''
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError
    return 2 * (a + b)