#crie um algoritmo que leia a idade de uma pessoa e diga em qual ano ela nasceu

#corriga o ano
#verificar se é maior de idade ou não
#perguntar ao usuário se quer continuar no final
#compare o mês agora

en = 'S'

while en in 'Ss':

    idade = int (input('Digite sua idade: '))
    mes1 = int (input('Digite o mês que nasceu: '))
    mesatual = int (input('Digite o mês atual: '))

   # ano = 2023 - idade
    #print(f'Você nasceu no ano de {ano}')

    if mes1 <= mesatual:
        print(f'Você nasceu no ano de {2023-idade}')
    elif mes1 > mesatual:
        print('Você nasceu no ano de',2023-1-idade)

    if idade >= 18:
        print('Você é maior de idade!')
    else:
        print('Você é menor de idade!')

    print ('Sua idade é: ',idade)

    en = str (input('Desejas continuar? (S/N) '))

#    if idade >=18 :
#        print('Você é maior de idade!')
#   else:
#   print('Você é menor de idade!')