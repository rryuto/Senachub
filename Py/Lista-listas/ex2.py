historico_senhas = ["1234", "senha123", "admin"]
nova_senha = input("Digite uma nova senha: ")

if nova_senha in historico_senhas:
    print("ERRO: Você já usou essa senha recentemente!")
else:
    print("Senha nova atualizada com sucesso!")
    historico_senhas.pop(0)
    historico_senhas.append(nova_senha)

#for senha in historico_senhas:
    #print(senha)