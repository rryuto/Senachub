usuarios_cadastrados = []
senhas_cadastradas = []
while True:
  
    print(f"\n  --MENU--  \n")
    print(f"1. Cadastrar Novo Usuário")
    print(f"2. Fazer Login")
    print(f"3. Sair\n")

    menu = int(input())
    if menu == 1:
            usuario = input("\nInsira um novo usuário: \n")

            if usuario in usuarios_cadastrados:
                print(f"\nERRO: Usuário já existente.")
            else:
                senha = input("\nUsuário válido.\nDigite uma senha:")
                usuarios_cadastrados.append(usuario)
                senhas_cadastradas.append(senha)
    elif menu == 2:
        usuario = input("\n --Login-- \nUsuário: ")
        if usuario in usuarios_cadastrados:    
            for i, nome in enumerate(usuarios_cadastrados):
                if usuario == usuarios_cadastrados[i]:
                    senha = input("Senha: ")
                    if senha == senhas_cadastradas[i]:
                        print("\nBem vindo!")
                    else:
                        print(f"\nAcesso negado.")
        else:
            print("\nUsuário não encontrado.")
    
    elif menu == 3:
        print("Saindo do programa.")
        break
    
    else:
        print("Opção invalida.")
