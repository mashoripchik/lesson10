from random import random, randint
a1 = []
a2 = []
for i in range(10):
    a1.append(randint(0, 5))
    a2.append(randint(-5, 0))
a1 = tuple(a1)
a2 = tuple(a2)
c = a1 + a2
print((c), c.count(0))

