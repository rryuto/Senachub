produtos = []
id_atual = 1

while True:
    print("1. Cadastrar produtos")
    print("2. Consultar por ID")
    print("3. Relatório geral")
    print("4. Sair")
    opcao = input()
    

    if opcao == '1':
        while True:
            print(" - CADASTRO - ")
            #ID automatico ou ID inserido?
            
            nome = input("Nome do produto: ")
            if nome == '0':
                break
            else:
                preco = int(input("Preço do produto: "))
                produto = {"id" : id_atual, "nome" : nome, "preco" : preco}
                produtos.append(produto)
                id_atual += 1

    elif opcao == '2':
        
        print(" - CONSULTAR - ")
        
        id_busca = int(input("Digite o ID do produto: "))

        encontrado = False
        
        for i in produtos:
            if i["id"] == id_busca:
                print(f"ID: {i["id"]}...{i["nome"]}...R${i["preco"]}")
                encontrado = True
                break
        if not encontrado:
            print("Produto não encontrado")

    elif opcao == '3':
        print(" - RELATORIO GERAL - ")

        for i in produtos:
            print(f"| Id: {i["id"]} | Produto: {i["nome"]} | Valor: {i["preco"]} |")   
        
    elif opcao == '4':
        print("Saindo.")
        break
