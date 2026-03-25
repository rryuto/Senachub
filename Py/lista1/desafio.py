saldo = 1000
limite_saque = 500
nome_cliente = "Claudio"
saque = 0
senha_correta = "1234"

print(f"Boas vindas {nome_cliente}! Seu saldo é de {saldo}R$. E seu limite de saque por operação é de {limite_saque}R$.")
pin = input("Por favor digite a senha: ")

if pin == senha_correta:
    saque = int(input("Qual o valor que deseja sacar? "))

    if saque <= saldo and saque <= limite_saque:
            if saque > 0 and saque % 10 == 0:
                    saldo = saldo - saque
                    print(f"Saque realizado com sucesso! Seu novo saldo é {saldo}R$")
            else:
                    print("O valor é invalido para as notas disponiveis.")
    elif saque > 500:
            print("Valor de saque é maior que o limite.")
    else:
            print("Saldo insuficiente.")
else:
       print("Senha incorreta.")        