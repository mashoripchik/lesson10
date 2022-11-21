from random import random, randint
a = tuple(randint(0, 100) for i in range(10))
print(a, 'min', min(a), 'max', max(a))