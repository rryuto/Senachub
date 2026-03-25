vendas = {
    "Eletronicos": 100, 
    "Roupas": 200,
    "Alimentos": 300
}

for chave, valor in vendas.items():
    print(f"Categoria: {chave} - Total: R${valor}")