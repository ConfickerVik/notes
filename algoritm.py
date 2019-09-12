import random
import math

def mk(y, a, m):
	x = (a * y) % m
	return int(x)
	
a = 630360016
m = 2147483647
A = list()
n = 3000
Xs = 0.0
X1 = 0
i = 0
keys = 0

x0 = int(input('Введите начальное значение Х: '))

for j in range(0, n-1):
	X1 = mk(x0, a, m)
	Xs += X1/m
	A.append(X1)
	x0 = X1

Xs = Xs/n
	
print(Xs)

i = math.ceil(n*random.random())

print(i)

keys = A[i]

print("Ключ: ", keys)