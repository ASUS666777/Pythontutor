''' Дан список, упорядоченный по неубыванию элементов
в нем. Определите, сколько в нем различных элементов.'''

l = [int(s) for s in input().split()]
b = 0
c = 1

for i in l:
    if l[b] != l[b+1]:
        c += 1
    b += 1
    if b+1 == len(l):
         break
print(c)

'''
a = [int(i) for i in input().split()]
num_distinct = 1
for i in range(0, len(a) - 1):
    if a[i] != a[i + 1]:
        num_distinct += 1
print(num_distinct)
'''
