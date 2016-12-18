import random

a = [[random.randint(0, 9) for _ in range(5)] for _ in range(5)]
b = [[random.randint(0, 9) for _ in range(5)] for _ in range(5)]
c = [[x + y for x, y in zip(one, two)] for (one, two) in zip(a, b)]
d = [[x * y for x, y in zip(one, two)] for (one, two) in zip(a, b)]
print('1-я матрица:')
print(a)
print('2-я матрица:')
print(b)
print('сложение матриц:')
print(c)
print('умножение матриц:')
print(d)