# faça um algoritmo que receba 2 notas e calcule a média aritmética

# aprovado soma >= 7
# soma >=4 recuperação
# soma < 4 reprovado


#ao final, pergunte se o usuário deseja fazer novamente a média, e se for sim, prossiga de novo.

en = 'S'
while en in "Ss":

    nota1 = float (input('Digite sua primeria nota: '))
    nota2 = float (input('Digite sua segunda nota: '))

    soma = (nota1+nota2)/2

    if soma < 4:
        print(f'Você foi reprovado! Sua média foi: {soma}')

    if soma >=4 and soma <7:
        print(f'você está em recuperação! Sua média foi: {soma}')

    else:
        print(f'Você foi aprovado! Sua média foi: {soma}')

    en = str (input('Deseja continuar? (S/N): '))

# poderia fazer desta forma:
# if media>=7:
#   print('Aprovado')
# elif media >= 4:
#   print('Recuperação')
# else:
#   print ('Reprovado')

# em outras linguagens:
#while en == "s" or en == "S":