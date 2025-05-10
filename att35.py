#crie um algoritmo que receba 3 números e informe qual o maior entre eles.


n1 = int (input('Digite o 1a número: '))
n2 = int (input('Digite o 2a número: '))
n3 = int (input('Digite o 3a número: '))

if n1 > n2:
    if n1 > n3:
        print('Número 1 é maior!')

if n2 > n1:
    if n2 > n3:
        print('Número 2 é maior!')

if n3 > n1:
    if n3 > n2:
        print('Número 3 é maior!')

# código do fessor:
# comparou o 1a e o 2a, para então comparar com 3a. eliminação.
#if n1 > n2:
#    if n1 > n3:
#        print(n1)
#    else:
#        print(n3)
#
#elif n2 > n3:
#    print(n2)
#
#else:
#    print (n3)