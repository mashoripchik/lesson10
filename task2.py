from random import random, randint
a = tuple([randint(0,5) for a in range(10)]) + tuple([randint(-5,0) for a in range(10)])
print(a, a.count(0))