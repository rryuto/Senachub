prox_cliente = 2
pedidos = {
    1 : {"cliente" : "rodrigo", 
         "item" : [{"nome" : "Teclado", "preco" : 100.0, "quantidade" : 1},
                   {"nome" : "Mouse", "preco" : 50.0, "quantidade" : 2}
                   ], "total" : 200.0} 
}

  #criar pedido
cliente = input("Nome do cliente: ")
#adicionar itens?
adicionar = input("Deseja adicionar itens ao carrinho?(s/n)")
if adicionar == 's':
    nome = input("Nome do produto: ")
    preco = float(input("Preço: "))
    quantidade = int(input("quantidade"))

    pedidos.append({2}) 
print(pedidos)