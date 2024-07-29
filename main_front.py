import flet as ft
import armazenamento


def main(page):
    estoque = armazenamento.ler()
    titulo = ft.Text('Gerenciamente de Estoque', theme_style=ft.TextThemeStyle.BODY_LARGE)
    
    def fechar_erro(e):
        Erro.open = False
        page.update(Erro)

    def fechar_produto(e):
        Produto_cadastrado.open = False
        page.update(Produto_cadastrado)
    
    titulo_erro = ft.Text('Erro!')
    campo_erro = ft.Text('Informações Inválidas!')
    campo_produto_ja_cadastrado = ft.Text('Produto já Cadastrato!')
    botao_fechar = ft.ElevatedButton('FECHAR!', on_click=fechar_erro)
    Erro = ft.AlertDialog(title=titulo_erro, content=campo_erro, actions=[botao_fechar])
    botao_produto = ft.ElevatedButton('FECHAR!', on_click=fechar_produto)
    Produto_cadastrado = ft.AlertDialog(title=titulo_erro, content=campo_produto_ja_cadastrado, actions=[botao_produto])



    def remover_item_do_estoque(e):
        page.remove(Botões)

        def sair_do_remover_item(e):
            page.remove(descobrir_item, botoes_do_remover_item)
            page.add(Botões)

        def remover_item(e):
            nome_produto = produto
            print(nome_produto)

        def procurar_item(e):
            global produto
            produto_procurado = descobrir_item.value
            produto_procurado = produto_procurado.strip().capitalize()
            cont = 0
            numerador = -1
            num = 0
            for item in estoque:
                for produto in item:
                    if produto_procurado in produto:
                        if num == 0:
                            page.remove(descobrir_item, botoes_do_remover_item)
                        numerador = cont
                        botao_remover = ft.ElevatedButton(produto, on_click=remover_item)
                        #estoque.pop(numerador)
                        #armazenamento.escrever(estoque)
                        page.add(botao_remover)
                        num = 1
                    else:
                        cont = cont + 1
            if numerador == -1:
                Erro.open = True
                page.add(Erro)

        descobrir_item = ft.TextField(label='Procurar Item')

        botao_procurar = ft.ElevatedButton('Procurar', on_click=procurar_item)
        botao_sair = ft.ElevatedButton('Sair', sair_do_remover_item)
  
        botoes_do_remover_item = ft.Row([botao_procurar, botao_sair])

        page.add(descobrir_item)
        page.add(botoes_do_remover_item)

    def modificar_item(e):
        page.remove(Botões)

        def sair_do_modificar_item(e):
            page.remove(descobrir_item,botoes_do_modificar_item)
            page.add(Botões)

        def produto_encontrado_do_modificar():
            def sair(e):
                page.remove(alterar_descricao, alterar_valor, alterar_quantidade, botoes)
                page.add(Botões)

            def salvar(e):
                if alterar_descricao.value != '':
                    nova_descricao = alterar_descricao.value
                    nova_descricao = nova_descricao.strip().capitalize()
                    estoque[numerador][produto_procurado]['descricao'] = nova_descricao
                
                if alterar_valor != '':
                    try:
                        novo_valor = alterar_valor.value.strip()
                        novo_valor = novo_valor.replace(',', '.')
                        novo_valor = float(novo_valor)
                    except:
                        cont = 0
                    else:
                        estoque[numerador][produto_procurado]['valor'] = novo_valor
                        cont = 1
                
                if alterar_quantidade != '':
                    try:
                        nova_quantidade = alterar_quantidade.value.strip()
                        nova_quantidade = int(nova_quantidade)
                    except:
                        cont = 0
                    else:
                        estoque[numerador][produto_procurado]['quantidade'] = nova_quantidade
                        cont = 1

                armazenamento.escrever(estoque)
                if cont == 1:
                    page.remove(alterar_descricao, alterar_valor, alterar_quantidade, botoes)
                    page.add(Botões)
                else:
                    Erro.open = True
                    page.add(Erro)

            global alterar_descricao, alterar_valor, alterar_quantidade
            alterar_descricao = ft.TextField(label='Nova Descrição')
            alterar_valor = ft.TextField(label='Novo Valor')
            alterar_quantidade = ft.TextField(label='Nova Quantidade')

            botao_salvar_alteracao = ft.ElevatedButton('Salvar Alteração', on_click=salvar)
            botao_sair_sem_salvar = ft.ElevatedButton('Sair sem Salvar', on_click=sair)
            botoes = ft.Row([botao_salvar_alteracao, botao_sair_sem_salvar])

            page.add(alterar_descricao, alterar_valor, alterar_quantidade, botoes)
            
        def procurar_item(e):
            global numerador, produto_procurado
            produto_procurado = descobrir_item.value
            produto_procurado = produto_procurado.strip().capitalize()
            cont = 0
            numerador = -1
            for item in estoque:
                for produto in item:
                    if produto_procurado in produto:
                        page.remove(descobrir_item, botoes_do_modificar_item)
                        numerador = cont
                        produto_encontrado_do_modificar()
                    else:
                        cont = cont + 1
            if numerador == -1:
                Erro.open = True
                page.add(Erro)

        descobrir_item = ft.TextField(label='Procurar Item')

        botao_procurar = ft.ElevatedButton('Procurar', on_click=procurar_item)
        botao_sair = ft.ElevatedButton('Sair', on_click=sair_do_modificar_item)
 
        botoes_do_modificar_item = ft.Row([botao_procurar, botao_sair])

        page.add(descobrir_item)
        page.add(botoes_do_modificar_item)     

    def adicionar_item(e):
        def sair_do_adicionar_item(e):
            page.remove(campo_nome, campo_descricao, campo_valor, campo_quantidade, botoes_do_adicionar_itens)
            page.add(Botões)
            page.update()
            
        def sair_estoque_e_enviar_informacao(e):
            num = 0
            for item in estoque:
                for produto in item:
                    if campo_nome.value.strip().capitalize() == produto:
                        num = 1
            if campo_nome.value == '' or campo_descricao.value == '' or campo_valor.value == '' or campo_quantidade.value == '':
                Erro.open = True
                page.add(Erro)
            elif num == 1:
                Produto_cadastrado.open = True
                page.add(Produto_cadastrado)
            else:
                page.remove(campo_nome, campo_descricao, campo_valor, campo_quantidade, botoes_do_adicionar_itens)
                page.add(Botões)

                novo_nome = campo_nome.value
                novo_nome = novo_nome.strip().capitalize()
                nova_descricao = campo_descricao.value
                nova_descricao = nova_descricao.strip().capitalize()

                try:
                    valor = campo_valor.value
                    novo_valor = valor.replace(',', '.')
                    novo_valor = float(novo_valor)

                    quantidade = campo_quantidade.value
                    nova_quantidade = int(quantidade)
                except:
                    Erro.open = True
                    page.add(Erro)

                produto_novo = {novo_nome : 
                    {'descricao' : nova_descricao,
                    'valor' : novo_valor,
                    'quantidade' : nova_quantidade}}
                
                estoque.append(produto_novo)
                armazenamento.escrever(estoque)
        
        page.remove(Botões)
        campo_nome = ft.TextField(label='Nome do Produto')
        campo_descricao = ft.TextField(label='Descrição do Produto')
        campo_valor = ft.TextField(label='Valor do Produto')
        campo_quantidade = ft.TextField(label='Quantidade do Produto')

        eniar_informacoes = ft.ElevatedButton('Salvar Produto', on_click=sair_estoque_e_enviar_informacao)
        botao_sair = ft.ElevatedButton('Sair', on_click=sair_do_adicionar_item)
        botoes_do_adicionar_itens = ft.Row([eniar_informacoes, botao_sair])

        page.add(campo_nome, campo_descricao, campo_valor, campo_quantidade)
        page.add(botoes_do_adicionar_itens)
        
    def ver_estoque(e):
        def sair_estoque(e):
            page.remove(botao_sair_estoque, tabela_do_estoque)
            page.add(Botões)

        page.remove(Botões)
        
        colunas = [
            ft.DataColumn(label=ft.Text('Produto')),
            ft.DataColumn(label=ft.Text('Descrição')),
            ft.DataColumn(label=ft.Text('Valor')),
            ft.DataColumn(label=ft.Text('Quantidade'))
            ]
        
        linhas = []
        for item in estoque:
            for nome_produto, detalhes_produto in item.items():
                linha = ft.DataRow(cells=[
                    ft.DataCell(ft.Text(nome_produto)),
                    ft.DataCell(ft.Text(detalhes_produto['descricao'])),
                    ft.DataCell(ft.Text(detalhes_produto['valor'])),
                    ft.DataCell(ft.Text(detalhes_produto['quantidade'])),
                    ]
                )
                linhas.append(linha)
        
        tabela_do_estoque = ft.DataTable(columns=colunas, rows=linhas)

        botao_sair_estoque = ft.ElevatedButton('Sair do Estoque', on_click=sair_estoque)

        page.add(botao_sair_estoque)
        page.add(tabela_do_estoque)
        
    def sair(e):
        page.window_close()   

    botao_1 = ft.ElevatedButton('Ver Estoque', on_click=ver_estoque)
    botao_2 = ft.ElevatedButton('Adicionar Item', on_click=adicionar_item)
    botao_3 = ft.ElevatedButton('Modificar Estoque', on_click=modificar_item)
    botao_4 = ft.ElevatedButton('Remover Item', on_click=remover_item_do_estoque)
    botao_5 = ft.ElevatedButton('Sair', on_click=sair)
    Botões = ft.Row([botao_1, botao_2, botao_3, botao_4, botao_5])

    page.add(titulo)
    page.add(Botões)

ft.app(main)
