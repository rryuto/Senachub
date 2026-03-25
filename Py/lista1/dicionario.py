#dicionario
#um dicionario é uma funcão que guarda chave -> valor

#exemplo simples

# pessoa = {
#     "nome": "Carlos",
#     "idade": 25
# }

# print(pessoa["nome"])
# print(pessoa["idade"])

#Cardapio usando dicionario em tupla. Tupla significa que guarda vários valores juntos.
cardapio = {
    1 : ("Hamburguer", 15),
    2 : ("Pizza", 30),
    3 : ("Refrigerante", 8)
}
#descompactamento
nome, preco = cardapio[1]
print(nome)
print(preco)

