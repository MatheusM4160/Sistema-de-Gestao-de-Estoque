import flet as ft

lista = [
    {'produto': 'tecido',
     'data': 2308},
    {'produto': 'tinta',
     'data': 2408}
]

def main(page):
    lista_check = []
    for dicionario in lista:
        data = str(dicionario['data'])
        dia = data[:2]
        mes = data[2:]
        data_modificada = f'{dia}/{mes}'
        check = ft.Checkbox(label=f"{dicionario['produto']} - {data_modificada}", value=False)
        lista_check.append(check)
    for x in lista_check:
        page.add(x)

ft.app(main)