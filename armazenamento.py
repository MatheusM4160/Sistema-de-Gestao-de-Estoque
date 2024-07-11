# Funções para ler e escrever os dados
import json

def ler():
    """Função para ler os dados em .json e retornar um dicionario"""
    with open('Dados/dados.json', 'r') as arq:
        return json.load(arq)

def escrever(dic):
    with open('Dados/dados.json', 'w') as arq:
        json.dump(dic, arq, indent=2)