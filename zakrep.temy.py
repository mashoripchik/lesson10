#1. Создайте  кортеж с цифрами от 0 до 9 и посчитайте сумму
from random import random, randint
a = tuple(randint(0, 9) for i in range(10))
print(a, sum(a))

#2. Выведите статистику частности букв в кортеже
long_word = ( 'т', 'т', 'а', 'и', 'и', 'а', 'и',
	         'и', 'и', 'т', 'т', 'а', 'и', 'и',
	         'и', 'и', 'и', 'т', 'и')
for i in set(long_word):
    print(f'{i} - {long_word.count(i)}')

#3. Допишите скрипт для расчета средней температуры
# Постарайтесь посчитать количество дней на основе week_temp.
# Так наш скрипт сможет работать c данными за любой период
week_temp = (26, 29, 34, 32, 28, 26, 23)
sum_temp = sum(week_temp)
days = len(week_temp)
mean_temp = sum_temp / days
print(int(mean_temp))
