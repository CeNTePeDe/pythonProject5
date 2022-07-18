def get(value):
    if value > 0:
        return  'positive'
    if value < 0:
        return  'negative'
    return 'zero'

if __name__ == '__main__':
    k = 0
    for _ in range(10):
        k = k+1
    value = int(input('ввести значение  '))
    print(get(value).upper())