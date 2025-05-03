#Escreva um algoritmo para ler 10 números e ao final da leitura escrever a média

#dos 10 números lidos.

resul=0
for x in range (0,10):
    numeros = float(input('Digite 10 números: '))
    resul = resul + numeros

print(resul/10)