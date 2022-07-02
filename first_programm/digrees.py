def get(value):
    if value > 0:
        return  'positive'
    if value < 0:
        return  'negative'

if __name__ == '__main__':
    value = int(input())
    print(get(value).upper())