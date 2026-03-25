sistema = []

while True:
    
    op = input("Digite uma opção:\n 1.Cadastro\n2.Login\n3.Sair\n")
    
    if op == "1":
        id = input("Digite um login: \n")
        existe = False
        for i in sistema:
            if i["usuario"] == id:
                existe = True
        
        if existe == True:
            print("Usuario ja existe!")
        else:
            senha = input("digite uma senha: \n")
            sistema.append({
                "usuario" : id,
                "senha" : senha
            })

    if op == "2":
        id = input("Digite um usuário: \n")
        senha = input("Digite uma senha: \n")
        for i in sistema:
            if i["usuario"] == id and i["senha"] == senha:
                print("Login realizado com sucesso!")
            
    if op == "3":
        print("Programa encerrado.")
        break