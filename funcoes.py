def LeiaInteiros(pergunta):
    while True:
        try:
            numero = int(input(pergunta))
        except:
            print('Digite um número válido!')
        else:
            return numero
            break    

def interface(titulo = 'TITULO', lista = [], quant = 40):    
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
    