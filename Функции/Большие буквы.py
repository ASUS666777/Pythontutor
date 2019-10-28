''' Напишите функцию capitalize(), которая принимает слово из
маленьких латинских букв и возвращает его же, меняя первую букву на большую.
Например, print(capitalize(‘word’)) должно печатать слово Word.
На вход подаётся строка, состоящая из слов, разделённых одним пробелом.
Слова состоят из маленьких латинских букв. Напечатайте исходную строку, сделав так,
чтобы каждое слово начиналось с большой буквы. При этом используйте вашу функцию capitalize().

Напомним, что в Питоне есть функция ord(), которая по символу возвращает его код в таблице ASCII,
и функция chr(), которая по коду символа возвращает сам символ. Например, ord('a') == 97, chr(97) == 'a'.
'''


def capitalize():
    t = s.count(' ')
    if t < 1: # если нет пробелов
        b = []
        for i in range(len(s)):
            new_element = s[i]
            b.append(new_element)
            if b[i] == ' ' or i == len(s)-1:
                d = ord(b[0])
                c = d - 32
                d, b[0] = b[0], chr(c)
                break
    else: # если пробелы есть
        b = []
        for i in range(len(s)):
            new_element = s[i]
            b.append(new_element)
            if b[i] == ' ':
                d = ord(b[0])
                c = d - 32
                d, b[0] = b[0], chr(c)
                break
            
        for a in range(i+1,len(s)):
            new_element = s[a]
            b.append(new_element)
            if s[a] == ' ' or a == len(s)-1:
                q = ord(b[i+1])
                w = q - 32
                q, b[i+1] = b[i+1], chr(w)
                
    
    
    
    return(''.join([str(i) for i in b]))
    
    
    
s = input()
print(capitalize())



'''
# правильное решение
def capitalize(word):
    first_letter_small = word[0]
    first_letter_big = chr(ord(first_letter_small) - ord('a') + ord('A'))
    return first_letter_big + word[1:]
 
source = input().split()
res = []
for word in source:
    res.append(capitalize(word))
print(' '.join(res))
'''


