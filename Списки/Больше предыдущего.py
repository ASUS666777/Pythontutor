'''Дан список чисел. Выведите все элементы списка,
которые больше предыдущего элемента.'''

l = [int(s) for s in input().split()]
b = 0
for a in l:
    x = l[b]
    y = l[b+1]
    if x < y:
        print(y, end =' ')
    b += 1
    c = int(len(l))
    if b == (c-1):break
