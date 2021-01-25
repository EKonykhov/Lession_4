#=====#1=====

from sys import argv

production, rate, premium = argv

try:
    production = int(production)
    rate = int(rate)
    premium = int(premium)

    x = production * rate + premium

    print(f"Result: {x}")

except ValueError:
    print("Please enter a number")


#=====#2=====

x = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
y = [i for n,i in enumerate (x) if x[n]> x[n-1]]
print(f'Result: {y}')

#=====#3=====

print(f'Result: {[i for n,i in enumerate (range (20,241)) if i % 20 ==0 or i % 21 ==0]}')

#=====#4=====

x = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(f'Result: {[i for n,i in enumerate (x) if x.count(i)==1]}')

#=====#5===== Ничего себе циферка перемножения )))

from functools import reduce
y = 2  #Четные числа
x = range(100,1001,y)
z = [i for n,i in enumerate (x)]
print(f'Result: {reduce(lambda q,w: q * w,[i for n,i in enumerate (range(100,1001,2))])}')

#  Вот интересно а можно и вовсе импортировать редус() в строку? Что бы решение, одной строкой было?
#from functools import reduce
#print(f'Result: {reduce(lambda q,w: q * w,[i for n,i in enumerate (range(100,1001,2))])}')

#=====#6=====
import itertools

n = 10

for trampampam in itertools.count(3):
    if trampampam > n:
        break
    else:
        print(trampampam, end=' ')

x = 0
for trampampam in itertools.cycle("ABC"):
    x += 1
    if x > n:
        break
    print(trampampam, end=' ')

#=====#7=====

import math

n = 10

def fact():
    for i in range(1,n):
        yield math.factorial(i)

for i in fact():
    print(f"Компил: {fact()}, Факториал: {i}")