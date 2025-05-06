#pergunta ao usuário a quantidade de número, calcular e escrever a média aritmética desses valores lidos

#usando while

vezes = int (input('Quantas notas gostaria de adicionar: '))

x=1
notas=0
soma=0

while x <= vezes:
    notas = float (input('Digite sua nota: '))
    x = x + 1
    soma = soma + notas

media = soma/vezes
print('Sua média é: ',media)
