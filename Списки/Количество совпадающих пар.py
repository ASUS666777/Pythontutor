''' Дан список чисел. Посчитайте, сколько в нем пар элементов,равных друг другу.
Считается, что любые два элемента,равные друг другу образуют одну пару,
которую необходимо посчитать.
1 2 3 2 3 (ответ 2)

1 1 1 1 1 (ответ 10)

1 2 3 (ответ 0)

0 0 6 1 1 4 2 1 2 2 (ответ 7)'''




l = [int(s) for s in input().split()]

d = 0
e = 0
for i in range(e,len(l)):
    b = l[i]
    for c in range(e+1,len(l)):
        f = l[c]
        if b == f:
            d += 1
    e += 1
   
print(d)

'''
a = [int(s) for s in input().split()]
counter = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            counter += 1
print(counter)
'''
