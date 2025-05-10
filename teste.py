from re import match

verificacao = True

while verificacao:

    print('1 - Módulo Cliente')
    print('2 - Módulo Produto')
    print('3 - Módulo fornecedor')
    print('4 - Sair')

    menuOp = int(input('Escolha uma das opções: '))

    match (menuOp):
        case 1:
            print('A')
        case 2:
            print('B')
        case 3:
            print('C')
        case 4:
            print('Encerrando o programa...')
        case _:
            print('Opção inválida!')




