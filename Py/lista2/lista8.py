senha = "123"
while True:
    confere = input(("Senha: "))
    if confere == senha:
        print("Acesso válido")
        break
    else:
        print("Acesso negado tente denovo")