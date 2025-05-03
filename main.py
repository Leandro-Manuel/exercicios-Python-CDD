#problema:

#dados os valores de horários abaixo, decifre a lógica e faça um código para executar.
#entrada01 3:45
#entrada02 14:20
# a saída deve ser 6:05


h1 = int (input('Digite a hora: '))
m1 = int (input('Digite o minuto: '))
h2 = int (input('Digite a hora: '))
m2 = int (input('Digite o minuto: '))

htemp=0
minutos = m1+m2

if minutos>=60:
    htemp=1
    minutos=minutos-60

#tratando as horas

if h1 > 12:
    h1 = h1 - 12

if h2 > 12:
    h2 = h2 - 12

ht = h1 + h2 + htemp
mt = minutos

print (ht,  ":", mt)
