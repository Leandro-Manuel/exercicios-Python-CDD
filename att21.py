#ler uma variável de número inteiro e mostrar a tabuada de multiplicação

#desse número.

num = int (input('Digite um número: '))
for x in range (1,11):
    print(f"{x} x {num} = {num*x}")