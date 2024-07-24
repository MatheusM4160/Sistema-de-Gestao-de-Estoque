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

def adicionar(pergunta, num = 1):
        """Pegar o nome do produto novo"""
        while True:
            try:
                if num == 1:
                    nome = str(input(pergunta)).capitalize().strip()
                elif num == 2:
                    nome = float(input(pergunta))
                elif num == 3:
                    nome = int(input(pergunta))
            except:
                print('Nome invalido!')
            else:
                return nome

def Produto():   

    nome = adicionar('Nome do produto: ')
    
    descricao = adicionar('Descricao do produto: ')
        
    valor = adicionar('Valor do porduto: ', 2)

    quantidade = adicionar('quantidade do produto: ', 3)

    produto_novo = {nome : 
                 {'descricao' : descricao,
                  'valor' : valor,
                  'quantidade' : quantidade}}
    
    return produto_novo