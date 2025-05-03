#Receba 2 números do usuário e mostre eles em ordem crescente.

n1 = int (input('Digite um número: '))
n2 = int (input('Digite outro número: '))
if n2>n1:
    print(n1,n2)

else:
    print(n2,n1)

n1 = float (input('Digite sua primeira nota: '))
n2 = float (input('Digite sua segunda nota: '))
n3 = float (input('Digite sua terceira nota: '))
soma = (n1+n2+n3) /3
media = 0

if (n1<=10 and n2<=10 and n3<=10) and (n1>=0 and n2>=10 and n3>=10):
    if soma <7:
        if media <4:
            print('Aluno reprovado!')
        else:
            print('Aluno em recuperação!')
    else:
        print('Aluno aprovado!')
else:
    print('Digite valores maiores que 0 e menor que 10')

#Ler o nome de 2 times e o número de gols marcados na partida (para cada time)

#Escrever o nome do vencedor. Caso não haja vencedor deverá ser impressa a palavra EMPATE

time1 = (input('Digite o nome do seu time: '))
gol1 = int(input('Quantos gols marcou: '))
time2 = (input('Digite o nome do outro time: '))
gol2 = int(input('Quantos gols marcou: '))

if gol1 == gol2:
    print('EMPATE')
else:
    if gol1>gol2:
        print("O time",time1,"ganhou a partida!")
    else:
        print("O time",time2,"ganhou a partida!")

# Escreva um algoritmo que leia o número de litros vendidos e o tipo de combustível

# (codificado da seguinte forma: E-etanol, G-gasolina)
# Calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina
# É 5,80 e o preço do litro do etanol é 4,90.
#primeiramente pega-se o tipo de combustivel e a quantidade.

tipo = input('Qual é o seu combustível: ')
quantidade = float (input('Quantos litros gostaria de adicionar: '))


if tipo=="g":
    resultado1 = 5.80 * quantidade
    print('Valor a ser pago: ',resultado1)
elif tipo=="e":
        resultado2 = 4.90 * quantidade
        print('Valor a ser pago: ',resultado2)
else:
    print('Valor inválido')