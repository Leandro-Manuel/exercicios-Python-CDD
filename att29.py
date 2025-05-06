#ler 10 valores, calcular e escrever a média aritmética desses valores lidos

#usando while

x=1
notas=0
soma=0
while x <= 10:
    notas = float (input("Digite sua nota: "))
    x+=1
    soma+=notas
media = (soma/10)

print('Sua média final é: ',media)