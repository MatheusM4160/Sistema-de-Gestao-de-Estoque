# Funções para ler e escrever os dados
import json

def ler():
    """Função para ler os dados em .json e retornar um dicionario"""
    with open('Dados/dados.json', 'r') as arq:
        return json.load(arq)

def escrever(dic):
    """Função para escrever os dados em .json"""
    with open('Dados/dados.json', 'w') as arq:
        json.dump(dic, arq, indent=2)

def Adicionar():
    """Função para adicionar dados em um variavel"""
    def nome():
        """Pegar o nome do produto novo"""
        while True:
            try:
                nome = str(input('Nome do produto: ')).capitalize().strip()
            except:
                print('Nome invalido!')
            else:
                return nome
                break
    
    def descricao():
        """Pegar a descricao do produto novo"""
        while True:
            try:
                descricao = str(input('Descricao do produto: ')).capitalize().strip()
            except:
                print('Descricao invalida!')
            else:
                return descricao
                break

    def valor():
        """Pegar o valor do produto novo"""
        while True:
            try:
                valor = float(input('Valor do porduto: '))
            except:
                print('Valor invalido!')
            else:
                return valor
                break
    
    def quantidade():
        """Pegar a quantidade do produto novo"""
        while True:
            try:
                quantidade = int(input('quantidade do produto: '))
            except:
                print('Quantidade invalida')
            else:
                return quantidade
                break

    produto_novo = {nome() : 
                 {'descricao' : descricao(),
                  'valor' : valor(),
                  'quantidade' : quantidade()}}
    
    return produto_novo