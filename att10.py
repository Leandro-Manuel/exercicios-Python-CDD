nome = input('O seu nome é')
print('Seu nome é',nome)

nome1=input('digite o seu primeiro nome: ')
nome2=input('Digite o seu segundo nome: ')
nome3=input('Digite o seu último nome: ')
print(f" O seu nome completo é {nome1},{nome2},{nome3}")

Numero1 = int(input('Digite um número: '))
Numero2 = int(input('Digite outro número: '))
Resultado = Numero1+Numero2
print(Resultado)

#crie um programa para calcular a média de 2 notas e mostrar essa média e o nome do aluno

nome = input('Digite o seu nome: ')
nota1 = float(input('Digite sua primeira nota: '))
nota2 =float(input('Digite sua segunda nota: '))
resultado = (nota1+nota2)/2;
print(f'{nome} a sua nota final foi: {resultado}')

#Faça um programa para ler o nome de uma pessoa, a sua idade e o seu salário e mostre essas informações na tela.

nome = input('Digite o seu nome: ')
idade = int(input('Digite a sua idade: '))
salario = float(input('Digite o seu salário: '))
print(f'O seu nome é {nome}, você tem {idade} anos o seu salário atualmente é {salario}')
#Pegue o salário + 20% = resultado

salario = float(input('Digite o seu salário: '))
resultado = salario*1.2
print(f'O seu salário com aumento de 20% é: {resultado}')

#leia um salário e o aumento percentual que quer que aumente.

#filhos + 150 reais
salario = float(input('Digite o seu salário: '))
aumento = int(input('Digite a porcentagem de aumento do salário: '))
filhos = int(input('Quantos filhos tem: '))

resultado = (salario*(aumento/100))+salario;
acres = resultado+(filhos*150);
ferias = resultado/3;
print(f'O seu salário inicial é de {salario}, o salário com aumento de {aumento}% é {resultado}, com abono de {filhos} filho(s) {acres}, suas férias é {ferias}reais')