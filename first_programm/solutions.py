def square(a):
    y = a ** 2
    return y


if __name__ == '__main__':

    try:
        square(2)
    except:
        print('Message')
