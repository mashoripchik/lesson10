from random import random, randint
a = (1, 2, 3, 15, 4, 18, 25, 19, 5, 13)
print(max(a), min(a))
a1 = []
for i in range(10):
    a1.append(randint(0, 1000))
print(a1)
a1 = tuple(a1)
print(a1)
print('max', max(a1), 'min', min(a1))