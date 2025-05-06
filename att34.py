# input for print

# digite um número 5

# saída 1 22 333 4444 55555 usa-se end=" "

num = int (input('Digite um número: '))

for x in range (num+1):
    print ( x * str(x), end=" ")

#transformou o número em string
# valor do x inicial = 0

# imprima a saída

#1
#12
#123
#1234
#12345

num = int (input('Digite um número: '))

#primeiro valor de h = 0

for h in range (num+1):
    for y in range (1,h+1):
        print(y, end=" ")
    print()

# print() quebra linha

# imprima

#1 22 333 4444 55555
#usando o while

num = int (input('Digite um número: '))
cont = 1

while cont <= num:
    print(cont * str(cont), end=" ")
    cont+= 1

# imprima usando while:

#1 22 333 4444 55555

num = int (input('Digite um número: '))

n = 1

while n <= num:
    print (n*str(n),end=" ")
    n+=1

#imprima usando while

#1
#1 2
#1 2 3 ...

n = int (input('infome um número: '))

h=1
while h<=n:
    y=1
    while y<=h:
        print (y,end=" ")
        y+=1
    print()
    h+=1