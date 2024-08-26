import flet as ft
import armazenamento


def main(page):
    page.theme_mode = ft.ThemeMode.DARK

    estoque = armazenamento.ler()
    lista_pedidos = armazenamento.ler_pedidos()
    titulo = ft.Text('Gerenciamente de Estoque', theme_style=ft.TextThemeStyle.BODY_LARGE)
    
    #função para fechar o pop de erro
    def fechar_erro(e):
        Erro.open = False
        page.update(Erro)

    #função para fechar o pop de produto já cadastrado
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


    #função que é chamada após o botão de "remover item" ser acionada
    def remover_item_do_estoque(e):
        page.remove(Botões)

        def sair_do_remover_item(e):
            page.remove(descobrir_item, botoes_do_remover_item)
            page.add(Botões)
            page.update()

        def procurar_item(e):
            def voltar(e):
                for botao in lista_botoes:
                    page.remove(botao)
                page.remove(voltar_ao_inicio)
                lista_botoes.clear()
                page.add(Botões)

            def remover_item(produto, contador):
                estoque.pop(contador)
                armazenamento.escrever(estoque)
                for botao in lista_botoes:
                    page.remove(botao)
                page.remove(voltar_ao_inicio)
                lista_botoes.clear()
                page.add(Botões)

            voltar_ao_inicio = ft.ElevatedButton('Voltar', on_click=voltar)

            produto_procurado = descobrir_item.value
            produto_procurado = produto_procurado.strip().capitalize()
            
            lista_botoes = []
            cont = 0
            numerador = -1
            num = 0

            if descobrir_item.value != '':
                for item in estoque:
                    for produto in item:
                        if produto_procurado in produto:
                            if num == 0:
                                page.remove(descobrir_item, botoes_do_remover_item)
                                page.add(voltar_ao_inicio)
                            numerador = cont
                            botao_remover = ft.ElevatedButton(produto, on_click=lambda e, p=produto, cont=numerador: remover_item(p, cont)) 
                            lista_botoes.append(botao_remover)
                            page.add(botao_remover)
                            num = 1
                    cont = cont + 1
                if numerador == -1:
                    Erro.open = True
                    page.add(Erro)
            else:
                Erro.open = True
                page.add(Erro)           

        descobrir_item = ft.TextField(label='Procurar Item')

        botao_procurar = ft.ElevatedButton('Procurar', on_click=procurar_item)
        botao_sair = ft.ElevatedButton('Sair', on_click=sair_do_remover_item)
  
        botoes_do_remover_item = ft.Row([botao_procurar, botao_sair])

        page.add(descobrir_item)
        page.add(botoes_do_remover_item)

    #função para ver os pedidos, pendentes e concluidos, após o "Ver pedidos" ser clicado
    def ver_pedidos(e):
        page.remove(Botões)

        #vai sair da função "Ver pedidos" e caso o tenho alguma alteração do ""id"" vai mudar e salvar a nova alteração
        def sair_ver_pedidos(e):
            for check in lista_pendentes:
                valor = check['check']
                if valor.value == True:
                    lista_pedidos[check['index']]['id'] = 1
                else:
                    lista_pedidos[check['index']]['id'] = 0
            
            armazenamento.escrever_pedidos(lista_pedidos)

            page.remove(botao_sair)
            page.remove(abas)
            page.add(Botões)

        lista_pendentes = []
        lista_concluidos = []

        aba_pendentes = ft.Column()
        aba_concluidos = ft.Column()

        index = 0

        for pedidos in lista_pedidos:

            data = str(pedidos['data'])
            dia = data[:2]
            mes = data[2:]
            data_modificada = f"{dia}/{mes}"

            check = ft.Checkbox(label=f"{pedidos['produto']} - {data_modificada}", value=(pedidos['id'] == 1))

            produto_index = {'index': index,
                             'check': check}
            index = index + 1
            
            if pedidos["id"] == 0:
                lista_pendentes.append(produto_index)
                aba_pendentes.controls.append(check)
            elif pedidos["id"] == 1:               
                lista_concluidos.append(produto_index)
                aba_concluidos.controls.append(check)

        #logica para escrever as abas
        abas = ft.Tabs(
            selected_index=0,
            animation_duration=200,
            tabs=[
                ft.Tab(
                    text='Pendentes',
                    content=ft.Container(
                        content=ft.Column(
                            controls=[
                                aba_pendentes
                            ]
                        ),
                        padding=10
                    )
                ),
                ft.Tab(
                    text='Concluidos',
                    content=ft.Container(
                        content=ft.Column(
                            controls=[
                                aba_concluidos
                            ]
                        ),
                        padding=10
                    )
                )
            ]
        )

        botao_sair = ft.ElevatedButton('Sair', on_click=sair_ver_pedidos)

        page.add(botao_sair)
        page.add(abas)
        
    #função para adicionar pedidos após "Novo Pedido" for clicado
    def pedido_de_produto(e):
        page.remove(Botões)

        #remove as funcionalidas de "Novo Pedido" e adiciona os Botões iniciais
        def sair():
            page.remove(botoes_de_ação)
            page.remove(campo_informações)
            page.add(Botões)

        #salva novo pedido
        def salvar_pedido(e):
            produto = nome.value
            data = data_pedido.value.strip()
            novo_pedido = {'produto': produto,
                           'data': data,
                           'id': 0}
            lista_pedidos.append(novo_pedido)
            armazenamento.escrever_pedidos(lista_pedidos)
            sair()

        #funcionalidades da primeira aba
        botao_sair = ft.ElevatedButton('Sair', on_click=sair)
        salvar_inf = ft.ElevatedButton('Salvar Pedido', on_click=salvar_pedido)
        botoes_de_ação = ft.Row([botao_sair, salvar_inf])

        nome = ft.TextField(label='Novo Pedido')
        data_pedido = ft.TextField(label='DD MM')
        campo_informações = ft.Row([nome, data_pedido])
        
        #adiciona as funcionalidades a pagina
        page.add(botoes_de_ação)
        page.add(campo_informações)          

    #função que é acionada após o botão"alterar informação" ser clicado
    def alterar_informacoes_do_produto(e):
        page.remove(Botões)

        def sair_do_modificar_item(e):
            page.remove(descobrir_item,botoes_do_modificar_item)
            page.add(Botões)

        def produto_encontrado_do_modificar(a, b):
            for botao in lista_botao:
                page.remove(botao)
            page.remove(voltar_inicio)
            lista_botao.clear()

            def sair(e):
                page.remove(alterar_descricao, alterar_valor, alterar_quantidade, botoes)
                page.add(Botões)

            def salvar(produto, numero):
                cont = 1
                if alterar_descricao.value != '':
                    nova_descricao = alterar_descricao.value
                    nova_descricao = nova_descricao.strip().capitalize()
                    estoque[numero][produto]['descricao'] = nova_descricao
                
                if alterar_valor.value != '':
                    try:
                        novo_valor = alterar_valor.value.strip()
                        novo_valor = novo_valor.replace(',', '.')
                        novo_valor = float(novo_valor)
                    except:
                        cont = 0
                    else:
                        estoque[numero][produto]['valor'] = novo_valor
                        cont = 1
                
                if alterar_quantidade.value != '':
                    try:
                        nova_quantidade = alterar_quantidade.value.strip()
                        nova_quantidade = int(nova_quantidade)
                    except:
                        cont = 0
                    else:
                        estoque[numero][produto]['quantidade'] = nova_quantidade
                        cont = 1

                armazenamento.escrever(estoque)

                if cont == 1:
                    page.remove(alterar_descricao, alterar_valor, alterar_quantidade, botoes)
                    page.add(Botões)
                else:
                    Erro.open = True
                    page.add(Erro)

            alterar_descricao = ft.TextField(label='Nova Descrição')
            alterar_valor = ft.TextField(label='Novo Valor')
            alterar_quantidade = ft.TextField(label='Nova Quantidade')

            botao_salvar_alteracao = ft.ElevatedButton('Salvar Alteração', on_click=lambda e:salvar(a, b))
            botao_sair_sem_salvar = ft.ElevatedButton('Sair sem Salvar', on_click=sair)
            botoes = ft.Row([botao_salvar_alteracao, botao_sair_sem_salvar])

            page.add(alterar_descricao, alterar_valor, alterar_quantidade, botoes)
            
        def procurar_item(e):
            def voltar(e):
                for botao in lista_botao:
                    page.remove(botao)
                page.remove(voltar_inicio)
                lista_botao.clear()
                page.add(Botões)

            global lista_botao
            lista_botao = []

            global voltar_inicio
            voltar_inicio = ft.ElevatedButton('Voltar', on_click=voltar)

            produto_procurado = descobrir_item.value
            produto_procurado = produto_procurado.strip().capitalize()

            cont = 0
            numerador = -1
            num = 0

            if descobrir_item.value != '':
                for item in estoque:
                    for produto in item:
                        if produto_procurado in produto:
                            if num == 0:
                                page.remove(descobrir_item, botoes_do_modificar_item)
                                page.add(voltar_inicio)
                            numerador = cont
                            botao_item = ft.ElevatedButton(produto, on_click=lambda e, numerador=numerador, produto=produto: produto_encontrado_do_modificar(produto, numerador))
                            page.add(botao_item)
                            lista_botao.append(botao_item)
                            num = 1
                    cont = cont + 1
                if numerador == -1:
                    Erro.open = True
                    page.add(Erro)
            else:
                Erro.open = True
                page.add(Erro)

        descobrir_item = ft.TextField(label='Procurar Item')

        botao_procurar = ft.ElevatedButton('Procurar', on_click=procurar_item)
        botao_sair = ft.ElevatedButton('Sair', on_click=sair_do_modificar_item)
 
        botoes_do_modificar_item = ft.Row([botao_procurar, botao_sair])

        page.add(descobrir_item)
        page.add(botoes_do_modificar_item)     

    #Função que é chamada após o botão "alterar estoque" ser clicado
    def alterar_estoque(e):
        #remove os botoes iniciais da pagina
        page.remove(Botões)

        #remove as funcionalidades do "alterar_estoque" e adiciona os botões iniciais
        def sair(e):
            page.remove(descobrir_item, botoes_do_alterar_estoque)
            page.add(Botões)
        
        #função chamada após o botão "procurar" ser clicado
        def procurar(e):
            #função que tirar tudo da pagina e adiciona os botões iniciais a pagina
            def voltar(e):
                for botao in lista_botao:
                    page.remove(botao)
                page.remove(voltar_inicial)
                lista_botao.clear()
                page.add(Botões)

            #função mãe que vai alterar o estoque do item escolhido
            def alterar_quantidade(numerador, produto):
                #remove a lista de itens que são encontrados e limpa a lista
                for botao in lista_botao:
                    page.remove(botao)
                page.remove(voltar_inicial)
                lista_botao.clear()

                #função que retira as funcionalidades da pagina e adiciona os botões iniciais
                def sair_alterar_estoque(e):
                    page.remove(quantidade_desejada_para_remover)
                    page.remove(alteraçoes)
                    page.remove(sair_alterar)
                    page.add(Botões)
                
                #função que vai verificar o "valor" de "quantidade_desejada_para_remover"
                def checar_remover():
                    if quantidade_desejada_para_remover.value == '':
                        variavel = 1
                    else:
                        try:
                            variavel = int(quantidade_desejada_para_remover.value)
                        except:
                            Erro.open = True
                            page.add(Erro)

                    return variavel

                #função que aumenta o estoque do produto após o botão "aumentar" for acionado
                def aumentar_estoque(e):
                    aumentar = checar_remover()

                    quant = estoque[numerador][produto]['quantidade']
                    quant = quant + aumentar
                    estoque[numerador][produto]['quantidade'] = quant
                    armazenamento.escrever(estoque)
                    quantidade_atual.value = quant
                    page.update(quantidade_atual)

                #função que reduz o estoque do produto após o botão "diminuir" for acionado
                def diminuir_estoque(e):
                    diminuir = checar_remover()
                    quant = estoque[numerador][produto]['quantidade']
                    quant = quant - diminuir
                    estoque[numerador][produto]['quantidade'] = quant
                    armazenamento.escrever(estoque)
                    quantidade_atual.value = quant
                    page.update(quantidade_atual)
                
                #funcionalidades da pagina
                sair_alterar = ft.ElevatedButton('Sair', on_click=sair_alterar_estoque)
                quantidade_desejada_para_remover = ft.TextField(label="Quantidade desejada")
                aumentar = ft.IconButton(icon=ft.icons.ADD, on_click=aumentar_estoque)
                quantidade_atual = ft.Text(estoque[numerador][produto]['quantidade'], size=50)
                diminuir = ft.IconButton(icon=ft.icons.REMOVE, on_click=diminuir_estoque)
                alteraçoes = ft.Row([aumentar, quantidade_atual, diminuir])

                #adicina as funcionalidades a pagina
                page.add(sair_alterar)
                page.add(quantidade_desejada_para_remover)
                page.add(alteraçoes)
                page.update(quantidade_atual)
            
            #chama a funçã "voltar"
            voltar_inicial = ft.ElevatedButton('Voltar', on_click=voltar)

            produto_procurado = descobrir_item.value
            produto_procurado = produto_procurado.strip().capitalize()

            #variaveis
            lista_botao = []
            cont = 0
            numerador = -1
            num = 0

            #funcionalidade para procurar o item no estoque e dps adicionar eles a pagina
            if descobrir_item.value != '':
                for item in estoque:
                    for produto in item:
                        if produto_procurado in produto:
                            if num == 0:
                                page.remove(descobrir_item, botoes_do_alterar_estoque)
                                page.add(voltar_inicial)
                            numerador = cont
                            botao_item = ft.ElevatedButton(produto, on_click=lambda e, numerador=numerador, produto=produto: alterar_quantidade(numerador, produto))
                            page.add(botao_item)
                            lista_botao.append(botao_item)
                            num = 1
                    cont = cont + 1
                if numerador == -1:
                    Erro.open = True
                    page.add(Erro)
            else:
                Erro.open = True
                page.add(Erro)

        #caixa de texto para descobrir item
        descobrir_item = ft.TextField(label='Procurar Item')

        #botões para procurar o item ou sair do "alterar item"
        botao_procurar = ft.ElevatedButton('Procurar', on_click=procurar)
        botao_sair = ft.ElevatedButton('Sair', on_click=sair)
 
        #coloca os botões acima em uma linha
        botoes_do_alterar_estoque = ft.Row([botao_procurar, botao_sair])

        #adiciona as funcionalidades do "alterar estoque" à pagina
        page.add(descobrir_item)
        page.add(botoes_do_alterar_estoque)     
        
    #função que adiciona item ao estoque após o botão "adicionar" for clicado
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
        
    #função para ver o estoque após o botão "ver estoque" for clicado
    def ver_estoque(e):
        page.remove(Botões)

        def sair_estoque(e):
            page.remove(botao_sair_estoque, tabela_do_estoque)
            page.add(Botões)
        
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

    #todos os botões da pagina inicial
    botao_1 = ft.ElevatedButton('Ver Estoque', on_click=ver_estoque)
    botao_2 = ft.ElevatedButton('Adicionar Item', on_click=adicionar_item)
    botao_3 = ft.ElevatedButton('Alterar Estoque', on_click=alterar_estoque)
    botao_4 = ft.ElevatedButton('Alterar Informações', on_click=alterar_informacoes_do_produto)
    botao_5 = ft.ElevatedButton('Novo Pedido', on_click=pedido_de_produto)
    botao_6 = ft.ElevatedButton('Ver Pedidos', on_click=ver_pedidos)
    botao_7 = ft.ElevatedButton('Remover Item', on_click=remover_item_do_estoque)
    botao_8 = ft.ElevatedButton('Sair', on_click=sair)
    Botões = ft.Row([botao_1, botao_2, botao_3, botao_4, botao_5, botao_6, botao_7, botao_8])

    page.add(titulo)
    page.add(Botões)

ft.app(main)