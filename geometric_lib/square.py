def area(a):
    '''
    Вычисляет площадь квадрата.

    Arguments:
        a (float): сторона квадрата

    Return:
        float: площадь квадрата

    Пример:
        area(3) = 9
    '''
    if not isinstance(a, (int, float)):
        raise TypeError
    return a * a


def perimeter(a):
    '''
    Вычисляет периметр квадрата.

    Arguments:
        a (float): сторона квадрата

    Return:
        float: периметр квадрата

    Пример:
        perimeter(8) = 4 * 2
    '''
    if not isinstance(a, (int, float)):
        raise TypeError
    return 4 * a