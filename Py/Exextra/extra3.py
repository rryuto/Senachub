#dicionario principal
#chave sera o ID do pedido
#Valor sera outro dicionario
#cliente (string)  
# itens (lista de dicionários)  
# total (float) 
pedidos = {}
prox_cliente = 1
while True:
    print("-"*20)
    print("1.Criar pedido")
    print("2. Listar pedidos")
    print("3. Ver detalhes de um pedido")
    print("4. Atualizar item de um pedido")
    print("5. Remover item de um pedido")
    print("6. Deletar pedido")
    print("-"*20)
    opcao = int(input())

    if opcao == 1:
        #criar pedido
        cliente = input("Nome do cliente: ")
        novo_pedido = {"cliente" : cliente,
                                    "item" : [],
                                    "total": 0
                                    }
                    
        pedidos[prox_cliente] = novo_pedido

        #adicionar itens?
        adicionar = input("Deseja adicionar itens ao carrinho?(s/n) ")
        total = 0
        while adicionar == 's':
            nome_produto = input("Nome do produto: ")
            preco_produto = float(input("Preço: "))
            quantidade_produto = int(input("Quantidade: "))
            novo_item = {"nome" : nome_produto, "preco" : preco_produto, "quantidade" : quantidade_produto}
            total = total + preco_produto*quantidade_produto
            pedidos[prox_cliente]["total"] = total
            pedidos[prox_cliente]["item"].append(novo_item)
            adicionar = input("Deseja adicionar mais itens ao carrinho?(s/n) ")
        prox_cliente += 1

    elif opcao == 2:
        #Listar pedidos
        #ID, cliente, total, quantidade de itens
        print("-"*20)
        for chave, valor in pedidos.items():
            total_quantidade = 0
            for item in valor["item"]:
                total_quantidade += item["quantidade"]

            print(f"{chave}: {valor["cliente"]} - Total: R${valor["total"]} Quantidade de itens: {total_quantidade}.")

    # elif opcao == 3:

    # elif opcao == 4:
    
    # elif opcao == 5:
    
    # elif opcao == 6:
    