from funcoes import *
from armazenamento import *

estoque = ler()

while True:
    opcao = interface('Gerenciamente de Estoque', ['Ver estoque', 'Adicionar item',
                'Modificar estoque', 'Remover item', 'Sair'], 40)
    
    if opcao == 1:
        for lista in estoque:
            for produto in lista:
                print(produto)
                print(f'>  {lista[produto]['descricao']}')
                print(f'>  R${lista[produto]['valor']}')
                print(f'>  {lista[produto]['quantidade']} unidades')

    elif opcao == 2:
        produto_novo = Adicionar()
        estoque.append(produto_novo)
        escrever(estoque)

    elif opcao == 3:
        pass

    elif opcao == 4:
        pass

    elif opcao == 5:
        print('Encerrando Sistema!')
        break

    elif opcao == 999:
        estoque.clear()
        escrever(estoque)

    else:
        print('Erro! opção inválida!')