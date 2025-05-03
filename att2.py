#faça um código para ler 2 valores e realize a divisão do primeiro pelo segundo

#valor recebido, caso o segundo valor digitado, seja zero, solicite novamente o valor
#informando que só aceitaremos valores diferentes de zero.
#se o usuário digitar zero 5 vezes printa um comando alertando que acabou

n1 = int (input('Digite o primeiro número: '))
n2 = int (input('Digite o segundo número: '))

vezes=1

while n2 == 0 and vezes<=5:

    n2 = int(input('Número inválido!' + "\n" + 'Digite um número diferente de zero: '))
    if vezes>=4:
        break
    vezes = vezes + 1

else:
    divisao = n1/n2
    print(divisao)
print('Programa finalizado')