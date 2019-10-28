'''Дано действительное положительное число a и целоe число n.

Вычислите a^n. Решение оформите в виде функции power(a, n).

Стандартной функцией возведения в степень пользоваться нельзя.

Например:
2
-3
Ответ 0.125

'''

def power(a, n):
    res = 1
    for i in range(abs(n)):
        res *= a
    if n >= 0:
        return res
    else:
        return 1 / res
 
print(power(float(input()), int(input())))
