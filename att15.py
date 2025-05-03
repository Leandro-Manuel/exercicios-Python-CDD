#escreva um algoritmo para ler 10 números e ao final da leitura escrever a soma

#total dos 10 números lidos.
soma=0
for x in range(0,10):
   numeros = int (input('Digite números: '))
   soma = soma + numeros
print(soma)