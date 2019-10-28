''' Выведите все четные элементы списка. При этом используйте цикл for,
перебирающий элементы списка, а не их индексы!'''

l = [int(s) for s in input().split()]
for element in l:
    if element%2 == 0:
        print(element, end =' ')
