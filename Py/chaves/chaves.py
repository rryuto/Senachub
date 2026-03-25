#chaves

#criando um dicionário

# carro = {
#     "marca": "Toyota",
#     "modelo": "Corola",
#     "ano": "2022"
# }

# print(f"O modelo do carro é: {carro['modelo']}")

# aluno = {"nome": "Lucas", "nota": 8.5}
# print(aluno["nome"])

# aluno["curso"] = "Python" #Se a chave não existe o python cria
# aluno["nota"] = 9.0 #Se ja existe e recebe valor, substitui

# print(aluno["curso"])
# print(aluno["nota"])

# #remover um item 2 formas

# del aluno["curso"] #apenas apaga
# nota_removida = aluno.pop("nota") #apaga e guarda na variavel

#percorrer chave com loop usandi item()

contato = {"Nome": "Ana", "Cidade": "Campo Grande"}

for chave, valor in contato.items():
    print(f"{chave}, {valor}")

