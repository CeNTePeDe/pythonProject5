from random import randint

N = 10
a = []
for i in range(N):
    a.append(randint(1, 99))
print(a)

for i in range(N - 1):
    for j in range(N - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)

N = 10
a = []
for i in range(N):
    a.append(randint(1, 99))
print(a)

i = 0
while i < N - 1:
    j = 0
    while j < N - 1 - i:
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
        j += 1
    i += 1
print(a)

N = 10
def bobble(array):
    for i in range(N - 1):
        for j in range(N - i - 1):
            if array[j] > array[j + 1]:
                #buff = array[j]
                #array[j] = array[j + 1]  a[j], a[j+1] = a[j+1], a[j]
                #array[j + 1] = buff
                array[j], array[j + 1] = array[j+1], array[j]
    return array




for i in range(N):
    a.append(randint(1, 99))
print(a)
bobble(a)
print(a)
