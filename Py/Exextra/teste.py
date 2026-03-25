prox_cliente = 2
pedidos = {
    1 : {
        "cliente" : "rodrigo", 
         "item" : [
                {"nome" : "Teclado", "preco" : 100.0, "quantidade" : 1},
                {"nome" : "Mouse", "preco" : 50.0, "quantidade" : 2}
            ], 
            "total" : 200.0
            }, 
    2 : {
        "cliente" : "rafael", 
         "item" : [
                {"nome" : "arroz", "preco" : 20.0, "quantidade" : 3},
                {"nome" : "Mouse", "preco" : 50.0, "quantidade" : 2}
            ], 
            "total" : 200.0
            }, 
    3 : {
        "cliente" : "renato", 
         "item" : [
                {"nome" : "Teclado", "preco" : 100.0, "quantidade" : 1},
                {"nome" : "Mouse", "preco" : 50.0, "quantidade" : 2}
            ], 
            "total" : 200.0
            } 
}

for chave, valor in pedidos.items():
    total_quantidade = 0
    for item in valor["item"]:
        total_quantidade += item["quantidade"]

    print(f"{chave}: {valor["cliente"]}  Total: {valor["total"]} qtd itens: {total_quantidade}")


# cliente = input("Nome do cliente: ")
# novo_pedido = {"cliente" : cliente,
#                                "item" : [],
#                                "total": 0
#                                }
               
# pedidos[prox_cliente] = novo_pedido

# print(pedidos)
# print(pedidos[1]["cliente"])
# print(pedidos[1]["item"][0]["nome"])
