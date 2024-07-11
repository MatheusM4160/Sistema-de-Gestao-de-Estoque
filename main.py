from armazenamento import *
from time import sleep
estoque = ler()['estoque']


def ver_itens():
    pass

def adicionar_itens():
    pass

def remover_itens():
    pass

print('-'*50)
print('Bem vindo ao Gerenciador de estoque'.center(50))
while True:
    print('-'*50)
    print('Opções:\n1. Ver estoque\n2. Adicionar novo item\n3. Modificar estoque de item'
          '\n4. Remover item\n0. Sair do Sistema')
    
    try:
        comando = int(input('Digite a opção: '))
    except:
        print('Erro! Digite uma opção válida')
    sleep(1)

    if comando == 0:
        print('\nEncerrando Sistema!')
        break

    elif comando == 1:
        print()
        print('-'*50)
        print('Produtos em estoque')
        print(f'\n{'Nome':<30}|{'valor':<6}  |quantidade')
        sleep(1)
        for produto in estoque:
            valor = estoque[produto]['valor']
            quantidade = estoque[produto]['quantidade']

            print(f'{produto:<30}|{valor:<6}  |{quantidade}')
            sleep(0.5)
        print()

    elif comando == 2:
        pass

    elif comando == 3:
        pass

    elif comando == 4:
        pass

    else:
        print('Opção inválida\n')