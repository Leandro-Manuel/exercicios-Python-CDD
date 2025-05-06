#faça um código para ler a senha de um usuário e após 3 tentativas erradas

# sair do programa, informando que a senha está bloqueada.

#agora mostre quantas tentativas o usuário tem

senha = str (input('Digite a sua senha: '))

verif = str (input('Digite a sua senha novamente: '))

cont = 1

while senha != verif:

    print(f"Você tem {3 - cont} tentativas restantes.")
    verif = str(input(f'Senha incorreta!'+"\n"+'Digite a sua senha novamente: '))

    if cont >= 2 and senha!=verif:
        print('Senha bloqueada!')
        break
    cont+=1
else:
    print('Senha correta!')