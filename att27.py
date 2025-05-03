#Ler 10 valores, calcular e escrever a média aritmética desses valores lidos.


soma=0
for x in range (10):
    numeros = int (input("Digite os números: "))
    soma += numeros
media = (soma/10)
print("A média aritmética é: ",media)