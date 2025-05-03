#Ler 10 valores e escrever quantos desses valores lidos estão no intervalo de (10,20)

#(incluindo os valores de 10 e 20 no intervalo) e quantos deles estão dentro deste intervalo.
dentro=0
for x in range (1,10):
    valores = int (input("Digite 10 números: "))
    if valores >=10 and valores<=20:
        dentro = dentro +1

fora = 10-dentro

print("os números que estão dentro: ",dentro)