# imprima a saída

#1
#12
#123
#1234
#12345

num = int(input('Digite um número: '))

#primeiro valor de h = 0

for h in range (num+1):
    for y in range (1,h+1):
        print(y, end=" ")
    print()

# print() quebra linha