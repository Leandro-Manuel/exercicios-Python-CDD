#receba do usuário, um número de 1 a 12 e mostre o nome do mês correspondente.

#caso o mês não existir, mostrar essa informação.

#primeiro trate a exceção primeiramente

mes = int (input('Digite o número do mês: '))

if mes <1 or mes>12:
    print('Número inválido. Digite entre 1 a 12')

if mes == 1:
    print('Janeiro')

if mes == 2:
    print('Fevereiro')

if mes == 3:
    print('Março')

if mes == 4:
    print ('Abril')

if mes == 5:
    print ('Maio')

if mes == 6:
    print ('Junho')

if mes == 7:
    print ('Julho')

if mes == 8:
    print ('Agosto')

if mes == 9:
    print ('Setembro')

if mes == 10:
    print ('Outubro')

if mes == 11:
    print ('Novembro')

if mes == 12:
    print ('Dezembro')