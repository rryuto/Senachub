#exercicio 1

#menu principal
carrinho = 0
quantidade_pedidos = 0
quantidade_hamburguer = 0
quantidade_pizza = 0
quantidade_refrigerante = 0
quantidade_batatafrita = 0
quantidade_milkshake = 0

while True:
  opcao = int(input("\n--- MENU PRINCIPAL ---\n1 - Ver Cardápio\n2 - Fazer Pedido\n3 - Ver total do pedido\n4 - Sair\n5 - Finalizar Pedido"))
  #opcao 1 Cardapio
  if opcao == 1:
    print("--- CARDÁPIO ---")
    print("1 - Hambúrguer - R$15")
    print("2 - Pizza - R$30") 
    print("3 - Refrigerante - R$8")
    print("4 - Batata frita - R$12")
    print("5 - Milkshake - R$10")
  #opcao 2 Fazer Pedido
  if opcao == 2:
    quantidade = None
    pedido = input("Adicionar ao pedido:\n")
    if pedido == "1":
      quantidade = int(input("Quantos Hamburgueres deseja?\n"))
      carrinho += 15*quantidade
      quantidade_pedidos += 1*quantidade
      quantidade_hamburguer += 1*quantidade
      print("Hamburguer adicionado ao pedido!")
    elif pedido == "2":
      quantidade = int(input("Quantas Pizzas deseja?\n"))
      carrinho += 30*quantidade
      quantidade_pedidos += 1*quantidade
      quantidade_pizza += 1*quantidade
      print("Pizza adicionado ao carrinho!")
    elif pedido == "3":
      quantidade = int(input("Quantos Refrigerantes deseja?\n"))
      carrinho += 8*quantidade
      quantidade_pedidos += 1*quantidade
      quantidade_refrigerante += 1*quantidade
      print("Refrigerante adicionado ao carrinho!")
    elif pedido == "4":
      quantidade = int(input("Quantas Batatas fritas deseja?\n"))
      carrinho += 12*quantidade
      quantidade_pedidos += 1*quantidade
      quantidade_batatafrita += 1*quantidade
      print("Batata fritas adicionado ao carrinho!")
    elif pedido == "5":
      quantidade = int(input("Quantos Milkshakes deseja?\n"))
      carrinho += 10*quantidade
      quantidade_pedidos += 1*quantidade
      quantidade_milkshake += 1*quantidade
      print("Milkshake adicionado ao carrinho!")
    else:
      print("Produto Inválido")
  #opcao 3 Ver total do carrinho
  if opcao == 3:
    print(f"Quantidade de produtos: {quantidade_pedidos}")
    print(f"Total do pedido: R${carrinho}")
  #opcao 4 Encerrar programa
  if opcao == 4:
    print("Encerrando o sistema\nObrigado pela preferência!")
    break
  #opcao 5 Finalizar pedido
  if opcao == 5:
    print("-- Resumo do pedido --")
    print(f"1 - Hamburgueres - {quantidade_hamburguer}")
    print(f"2 - Pizzas - {quantidade_pizza}") 
    print(f"3 - Refrigerantes - {quantidade_refrigerante}")
    print(f"4 - Batata fritas - {quantidade_batatafrita}")
    print(f"5 - Milkshake - {quantidade_milkshake}")
    print(f"\nQuantidade de produtos: {quantidade_pedidos}")
    print(f"Total do pedido: R${carrinho}")
    print(f"Obrigado pela compra!")
    break