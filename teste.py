lista_pedidos = [
  {
    "produto": "/",
    "data": "15/80/9515",
    "id": 0
  },
  {
    "produto": "/",
    "data": "15/08/7056",
    "id": 0
  },
  {
    "produto": "b/a",
    "data": "50/78/9562",
    "id": 0
  },
  {
    "produto": "Malha/Puro pano",
    "data": "24/12/2007",
    "id": 0
  }
]

cont = -1

for item in lista_pedidos:
    cont = cont + 1
    if item['produto'] == "Malha/Puro pano" and item['data'] == "24/12/2007":
        lista_pedidos.pop(cont)
        print(lista_pedidos)