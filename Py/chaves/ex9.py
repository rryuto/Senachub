menu = {
    "Parmegiana": 25,
    "Carreteiro": 18,
    "Feijoada"  : 20,
    "Hamburger" : 16,
    "Pastel"    : 14
}

lista =[]

opcao = 0

while opcao != "Sair":

    opcao = input("Selecione 1 para Ver Cardápio Completo\nSelecione 2 para Consultar Preço de um prato especifico.\nDigite 'Sair' para sair do programa.\n")

    if opcao == '1':
        print(f" -- MENU --")
        for chave, valor in menu.items():    
            print(f"{chave}.....{valor}")
    
    elif opcao == '2':
        prato = -1
        while prato != 0:     
            
            print("Consultar um prato.")
            
            for i, nome in enumerate(menu,start=1):
                print(f"{i} - {nome}")
                lista.append(nome)
            print("Digite '0' para voltar ao menu principal.")
            prato = int(input("Selecione um prato: "))
            
            if prato > 0 and prato < 6:
                selecao = lista[prato-1]
                print(f"{selecao}...R${menu[selecao]}")
            
            else:
                print("Opção inválida.")