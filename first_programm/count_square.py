from math import sqrt


def square_eq_solver(a, b, c):
    result = []
    discriminant = b ** 2 - 4 * a * c

    if discriminant == 0:
        result.append(-b / (2 * a))
    elif discriminant > 0:
        result.append((-b + sqrt(discriminant)) / (2 * a))
        result.append((-b - sqrt(discriminant)) / (2 * a))
    else:
        print(f'уровнение не имеет корней')
    return result


def show_result(data):
    if len(data) > 0:
        for index, value in enumerate(data):
            print(f'Корень номер {index + 1} равен {value:.02f}')
    else:
        print(f'Уровнение с заданными параметрами не имеет корней')


def main():
    try:
        a, b, c = (map(int, input('Введите числа через пробел: ').split()))

    except ValueError:
        print(("данные должны быть целочисленные"))
    else:
        result = square_eq_solver(a, b, c)
        show_result(result)
    finally:
        print("программа выполнена")


if __name__ == '__main__':
    main()
