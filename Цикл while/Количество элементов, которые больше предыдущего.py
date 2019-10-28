i = 0
b = 0
n = int(input())

while n != 0:
    i = n
    n = int(input())
    if n > i:
        b += 1

print(b)
