import flet as ft
import funcoes
import armazenamento


def main(page):
    estoque = armazenamento.ler()
    titulo = ft.Text('Gerenciamente de Estoque', theme_style=ft.TextThemeStyle.BODY_LARGE)
    
    def modificar_item(e):
        page.remove(Botões)
        

    def adicionar_item(e):        
        def sair_estoque_e_enviar_informacao(e):
            page.remove(campo_nome, campo_descricao, campo_valor, campo_quantidade, eniar_informacoes)
            page.add(Botões)

            novo_nome = campo_nome.value
            nova_descricao = campo_descricao.value

            valor = campo_valor.value
            novo_valor = valor.replace(',', '.')
            novo_valor = float(novo_valor)

            quantidade = campo_quantidade.value
            nova_quantidade = int(quantidade)

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

        page.add(campo_nome, campo_descricao, campo_valor, campo_quantidade)
        page.add(eniar_informacoes)
        page.update()

    def ver_estoque(e):

        def sair_estoque(e):
            page.remove(botao_sair_estoque, table)
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
        
        table = ft.DataTable(columns=colunas, rows=linhas)

        botao_sair_estoque = ft.ElevatedButton('Sair do Estoque', on_click=sair_estoque)

        page.add(botao_sair_estoque)
        page.add(table)
        page.update()

    def sair(e):
        page.window_close()   

    botao_1 = ft.ElevatedButton('Ver Estoque', on_click=ver_estoque)
    botao_2 = ft.ElevatedButton('Adicionar Item', on_click=adicionar_item)
    botao_3 = ft.ElevatedButton('Modificar Estoque', on_click=modificar_item)
    botao_4 = ft.ElevatedButton('Remover Item')
    botao_5 = ft.ElevatedButton('Sair', on_click=sair)
    Botões = ft.Row([botao_1, botao_2, botao_3, botao_4, botao_5])

    page.add(titulo)
    page.add(Botões)

ft.app(main)