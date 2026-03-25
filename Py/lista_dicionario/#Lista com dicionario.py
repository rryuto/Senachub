#Lista com dicionario

#sintaxe

usuarios = [
    {"nome" : "João", "senha" : "123"},
    {"nome" : "Maria", "senha" : "abc"}
]

# print(usuarios[0])

# print(usuarios[0]["nome"])

# print(usuarios[1]["senha"])

#percorrendo lista

for usuario in usuarios:
    print(usuario)

# #adicionando item 

# nome = input("Nome: ")
# senha = input("Senha: ")

# usuarios.append({
#     "nome": nome,
#     "senha": senha   
# })

# #exemplo login chatgpt

# 🔐 5. Exemplo de login (melhor que duas listas)
# usuarios = []

# while True:
#     print("\n1. Cadastrar")
#     print("2. Login")
#     print("3. Sair")

#     op = input("Opção: ")

#     if op == "1":
#         nome = input("Nome: ")

#         # verificar se já existe
#         existe = False
#         for u in usuarios:
#             if u["nome"] == nome:
#                 existe = True
#                 break

#         if existe:
#             print("Usuário já existe!")
#         else:
#             senha = input("Senha: ")
#             usuarios.append({"nome": nome, "senha": senha})
#             print("Cadastrado com sucesso!")

#     elif op == "2":
#         nome = input("Nome: ")
#         senha = input("Senha: ")

#         logado = False

#         for u in usuarios:
#             if u["nome"] == nome and u["senha"] == senha:
#                 logado = True
#                 break

#         if logado:
#             print("Bem-vindo!")
#         else:
#             print("Acesso negado.")

#     elif op == "3":
#         break