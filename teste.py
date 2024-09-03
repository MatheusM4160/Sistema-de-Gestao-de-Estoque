#a = 'Malha/Puro pano'
#print(a)
#b = a[:a.index('/')]
#a = a[a.index('/')+1:]
#print(b)
#print(a)

estoque = [
  {
    "Malha": {
      "descricao": "POLILINE BRA 91POLI-09ELAS250G",
      "valor": 28.0,
      "quantidade": 510,
      "fornecedor": "Textil farbe",
      "telefone": "(27)99997-9220"
    }
  },
  {
    "Malha": {
      "descricao": "POLILINE BRA 91POLI-09ELAS250G",
      "valor": 43.0,
      "quantidade": 153,
      "fornecedor": "Puro pano",
      "telefone": "(27)3721-6003"
    }
  },
  {
    "Tactel": {
      "descricao": "INDEFINIDO",
      "valor": 6.58,
      "quantidade": 230,
      "fornecedor": "Arteca",
      "telefone": "(27)3219-1341"
    }
  }
]

for item in estoque:
  for produto in item:
      print(produto)