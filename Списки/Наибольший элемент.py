''' Дан список чисел. Выведите значение наибольшего элемента в списке,
а затем индекс этого элемента в списке. Если наибольших элементов
несколько, выведите индекс первого из них.'''

l = [int(s) for s in input().split()]

a = max(l)
print(a, l.index(a))
