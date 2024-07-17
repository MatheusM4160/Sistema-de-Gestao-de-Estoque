from funcoes import *
from armazenamento import *


while True:
    estoque = ler()
    
    opcao = interface('Gerenciamente de Estoque', ['Ver estoque', 'Adicionar item',
                'Modificar estoque', 'Remover item', 'Sair'], 40)
    
    if opcao == 1:
        Ver_itens()

    elif opcao == 2:
        produto_novo = Adicionar()
        estoque.append(produto_novo)
        escrever(estoque)

    elif opcao == 3:
        Modificar()

    elif opcao == 4:
        Remover()

    elif opcao == 5:
        print('Encerrando Sistema!')
        break

    elif opcao == 999:
        estoque.clear()
        escrever(estoque)

    else:
        print('Erro! opção inválida!')