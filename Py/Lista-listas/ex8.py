#MENU
#adicionar
produtos = []
precos = []
opcao = 0
while opcao != '4':
    print("1. Adicionar produto")
    print("2. Ver carrinho")
    print("3. Remover produto")
    print("4. Encerrar")
    opcao = input("Seleciona a opção: ")
    if opcao == '1':
        produto = input("Informe o nome do produto: ")
        produtos.append(produto)
        preco = int(input("Informe o valor do produto: "))
        precos.append(preco)
    elif opcao == '2':
        for indice, item in enumerate(produtos):
                print(f"{indice} - {item} - R${precos[indice]}")
        print(f"Total do carrinho: {sum(precos)}")
    elif opcao == '3':
        deletar = int(input("Informe o número do item que deseja remover: "))
        produtos.pop(deletar)
        precos.pop(deletar)
    elif opcao == '4':
        print("Compra finalizada")
        print(f"Total: R${sum(precos)}")
        
