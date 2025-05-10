# crie um código que leia um número diferente de zero e diga se este número

#é positivo ou negativo.
# quando o usuário digitar 0, repita até digitar um número diferente
# no final, pergunte ao usuário se deseja fazer novamente o código e caso sim, prossiga.


en = 'S'
while en in 'Ss':

    num = int(input('Digite um número: '))
    while num == 0:
        num = int(input('Digite um número diferente de zero: '))

    if num <0:
        print(f'Seu número é negativo. {num}')
    else:
        print(f'Seu número é positivo! {num}')

    en = str (input('Desejas continuar? '))