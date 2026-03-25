controle = {
    "rafael": "12345",
    "rodrigo": "54321",
    "renato": "0000"
}

usuario = input("Digite o usuário:")


if usuario in controle:
    senha = input("Digite a senha: ")
    if senha == controle[usuario]:
        print("Acesso verificado")
    else:
        print("Senha incorreta")
else:
    print("Usuário não existe")