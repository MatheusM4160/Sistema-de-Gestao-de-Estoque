from armazenamento import *

def LeiaInteiros(pergunta):
    """Função para verificar se os numeros são inteiros ou não"""
    while True:
        try:
            numero = int(input(pergunta))
        except:
            print('Digite um número válido!')
        else:
            return numero
            break    

def interface(titulo = 'TITULO', lista = [], quant = 40):
    """Função para criar uma interface"""  
    print('-'*quant)
    print(f'{titulo}'.center(quant))
    print('-'*quant)
    cont = 1 
    for x in lista:
        print(f'{cont} - {x}')
        cont = cont + 1
    print('-'*quant)
    opcao = LeiaInteiros('Qual opção deseja? ')
    print('-'*quant)
    return opcao

def Ver_itens():
    """Função para ver os intens do estoque"""
    estoque = ler()
    for lista in estoque:
        for produto in lista:
            valor = str(lista[produto]['valor'])
            print(produto)
            print(f'>  {lista[produto]['descricao']}')
            print(f'>  R${valor.replace('.', ',')}')
            print(f'>  {lista[produto]['quantidade']} unidades')

def Modificar():
    """Modificar os itens do estoque"""
    estoque = ler()
    while True:
        try:
            pergunta = str(input('Qual o nome do produto? ')).capitalize().strip()
        except:
            print('Digite um nome válido!')
        else:
            break
    cont = 0
    numerador = -1
    for item in estoque:
        for produto in item:
            if produto == pergunta:
                descricao = item[produto]['descricao']
                numerador = cont
        cont =+ 1
    if numerador == -1:
        return print('Produto não encontrado! Tente novamente') 
    else:
        valor = float(input('Novo valor: '))
        quantidade = int(input('Nova quantidade: '))

        estoque[numerador] = {pergunta : {'descricao' : descricao,
                                            'valor' : valor,
                                            'quantidade' : quantidade}}
            
        escrever(estoque)
        return print('Alterado com Sucesso!')

def Remover():
    """Remover o item do estoque"""
    estoque = ler()
    while True:
        try:
            pergunta = str(input('Qual o nome do produto? ')).capitalize().strip()
        except:
            print('Digite um nome válido!')
        else:
            break
    cont = 0
    numerador = -1
    for item in estoque:
        for produto in item:
            if produto == pergunta:
                numerador = cont

        cont =+ 1
    if numerador == -1:
        return print('Produto não encontrado! Tente novamente') 
    else:       
        estoque.pop(numerador)
                
        escrever(estoque)
        return print('Removido com Sucesso!')