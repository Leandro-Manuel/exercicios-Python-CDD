# imprima

#1 22 333 4444 55555
#usando o while

num = int (input('Digite um número: '))
cont = 1

while cont <= num:
    print(cont * str(cont), end=" ")
    cont+= 1