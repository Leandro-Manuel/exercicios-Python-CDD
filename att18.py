#Ler um valor N e imprimir todos os valores inteiros entre 1 e N.

#considere que o N será sempre maior que zero.

N = int (input('Digite um número: '))
if N !=0:
    for x in range(1, N+1, 1):
        print(x, end=" ")
else:
    print('Digite um valor maior que 0')