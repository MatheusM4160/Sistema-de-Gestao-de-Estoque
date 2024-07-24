import funcoes
import armazenamento


while True:
    estoque = armazenamento.ler()
    
    opcao = funcoes.Interface('Gerenciamente de Estoque', ['Ver estoque', 'Adicionar item',
                'Modificar estoque', 'Remover item', 'Sair'], 40)
    
    if opcao == 1:
        funcoes.Ver_itens()

    elif opcao == 2:
        produto_novo = armazenamento.Produto()
        estoque.append(produto_novo)
        armazenamento.escrever(estoque)

    elif opcao == 3:
        funcoes.Modificar()

    elif opcao == 4:
        funcoes.Remover()

    elif opcao == 5:
        print('Encerrando Sistema!')
        break

    elif opcao == 999:
        estoque.clear()
        armazenamento.escrever(estoque)

    else:
        print('Erro! opção inválida!')