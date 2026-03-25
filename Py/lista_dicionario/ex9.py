carrinho = []

while True:
    print("1. Adicionar Item")
    print("2. Remover Item")
    print("3. Fechar conta")
    print("4. Sair")
    opcao = input()
    
    if opcao == '1':
        while True:
            print("- Adicionando pedido(Digite 0 para voltar ao menu) -")
            nome = input("Nome do produto: ")
            if nome == '0':
                break
            preco = int(input("Preco do produto: "))
            carrinho.append(
                {"nome" : nome, "preco" : preco}
            )


    elif opcao == '2':
        for i, item in enumerate(carrinho,start=1):
            print(f"{i} - {item["nome"]}...{item["preco"]}")
        remove = int(input("Remova um item pela numeração ou digite 0 para sair: "))  
        if remove == 0:
            continue
        else:
            carrinho.pop(remove-1)

    elif opcao == '3':
        total = 0
        for i in carrinho:
            total = total + i["preco"]
        
        print(f"Total: {total}")
    
    elif opcao == '4':
        print("Encerrando.")
        break