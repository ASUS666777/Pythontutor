i = 0
b = 0
n = int(input())

while n != 0:
    i += 1
    if n%2 == 0:
        b += 1
    n = int(input())  
print(b)
