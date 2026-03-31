#dicionario principal
#chave sera o ID do pedido
#Valor sera outro dicionario
#cliente (string)  
# itens (lista de dicionários)  
# total (float) 
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

    elif opcao == 3:
        id = int(input(f"Informe o ID do pedido: "))

        for chave, valor in pedidos.items():
        
            if chave == id:
                print(f"Pedido: {chave}")    
                for item in valor["item"]:
                    print(f"Item: {item["nome"]} - R${item["preco"]} - Quantidade : {item["quantidade"]}")
            
                print(f"Subtotal: {valor["total"]}")

    elif opcao == 4:
        id = int(input(f"Informe o ID do pedido: "))
        if id in pedidos:
            quantidade = 0
            for chave, valor in pedidos.items():
                if chave == id:
                    for item in valor["item"]:
                        print(f"Produto: {item["nome"]} -  Quantidade : {item["quantidade"]}")
                        quantidade = item["quantidade"]
            
            nome_item = input("Qual item deseja alterar? ")
            
            encontrado = False

            for item in pedidos[id]["item"]:
                if item["nome"].lower() == nome_item.lower():
                    alterar = int(input("Deseja alterar quantidade(1) ou preco(2)? "))

                    if alterar == 1:
                        nova_quantidade = int(input("Qual a nova quantidade?"))
                        item["quantidade"] = nova_quantidade
                    
                    elif alterar == 2:
                        novo_preco = float(input("Qual o novo preço? "))
                        item["preco"] = novo_preco

                    encontrado = True
            
            if not encontrado:
                print("Produto não encontrado")
            total = 0

            for item in pedidos[id]["item"]:
                total += item["preco"] * item["quantidade"]
            
            pedidos[id]["total"] = total
            print("Pedido atualizado com sucesso!")

        else:
            print("Pedido não encontrado")    
                          
    
    elif opcao == 5:
        id = int(input("Informe o Id do produto: "))

        encontrado = False

        if id in pedidos:
            nome_produto = input("Qual produto deseja remover? ")

            for i, item in enumerate(pedidos[id]["item"]):
                if item["nome"].lower() == nome_produto.lower():
                    pedidos[id]["item"].pop(i)
                    encontrado = True   
                    break

            if not encontrado:
                    print("Produto não encontrado")
            total = 0

            for item in pedidos[id]["item"]:
                total += item["preco"] * item["quantidade"]
            
            pedidos[id]["total"] = total
            print("Pedido atualizado com sucesso!")

        else:
            print("Pedido não encontrado")  

    elif opcao == 6:
        deletar = int(input("Qual pedido deseja deletar?"))

        del pedidos[deletar]
    