import logging
import doctest
logging.disable() # отключкение протоколирования

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Начало программы')


def factorial(n: int):
    """
    функция высчитывает факториалы от числа n
    :param n: int
    :return: total: int
    >>> factorial(5)
    120
    >>> factorial(3)
    6
    """
    logging.debug('Начало factorial(%s%%)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug(f'i = {i}, total = {total}')
    logging.debug('Конец factorial(%s%%)' % (n))
    return total


if __name__ == '__main__':
    #print(factorial(5))
    #doctest.testmod()
    print(factorial(0))
    logging.debug('end')
