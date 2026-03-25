estoque = {
    "item": "Pao frances",
    "preco": 0.50
}

estoque["preco"] = 0.60

for chave, valor in estoque.items():
    print(f"{chave}, {valor}")