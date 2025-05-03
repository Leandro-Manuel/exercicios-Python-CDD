#Ler 10 valores e escrever quantos desses valores lidos são negativos

# e contar quantos números negativos o usuário digitou
#somar todos os números negativos e mostrar o resultado, e todos os números positivos
negativos=0
soma=0
for x in range (1,11):
    num = int(input('Digite 10 números entre positivos e negativos: '))
    if num <0:
        negativos = negativos+1
        soma+=num

    if num<0:
        print(num)

positivos = (10-negativos)


print("Números negativos são: ",negativos,"\n","A soma dos números negativos são: ",soma,
      "\n","Números positivos: ",positivos)