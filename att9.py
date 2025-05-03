#escreva um código para ler as notas da 1a e 2a avaliações de um aluno,

#calcule e imprima a média desse aluno.
#só devem ser aceitos valores válidos, durante a leitura (0 a 10)
#para cada nota
#se o usuário quiser continuar com novas notas. prossiga

verificador ="y"
while verificador in "yY":

    nota1 = float(input('Digite sua primeira nota: '))

    while nota1 < 0 or nota1 > 10:
        nota1 = float(input('Digite sua primeira nota entre 0 a 10: '))

    nota2 = float(input('Digite sua segunda nota: '))

    while nota2 < 0 or nota2 > 10:
        nota2 = float(input('Digite sua segunda nota entre 0 a 10: '))


    media = (nota1+nota2)/2
    print('Sua média foi',media)
    verificador = input('desejas prosseguir com nova média? (y/n) ')