produtos = [
    {"nome": "arroz", "preco": 10, "quantidade": 5},
    {"nome": "feijao", "preco": 20, "quantidade": 10},
    {"nome": "batata", "preco": 30, "quantidade": 7},
    {"nome": "carne", "preco": 40, "quantidade": 8},
]

for i in produtos:
    print(f"Stock de {i["nome"]}: {i["preco"]*i["quantidade"]}")