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
    return 2 * (a + b)