''' Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию
distance(x1, y1, x2, y2), вычисляющая расстояние между точкой (x1,y1)
и (x2,y2). Считайте четыре действительных числа и выведите результат
работы этой функции. Если вы не знаете, как решить эту задачу, то вы,
возможно, не изучали в школе теорему Пифагора. Попробуйте прочитать
о ней на Википедии.

Например:

0
0
1
1
Ответ 1.41421

0.1
0.1
0.2
0.2
Ответ 0.141421 '''

from math import *

def dist(x1, y1, x2, y2):
    x = x2 - x1
    y = y2 - y1
    c = sqrt(x**2+y**2)
    return round(c, 5)

print(dist(float(input()), float(input()), float(input()), float(input())))

'''
from math import sqrt
 
def distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
 
x1 = float(input())
x2 = float(input())
y1 = float(input())
y2 = float(input())
print(distance(x1, x2, y1, y2))
'''
