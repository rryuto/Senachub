#listas

frutas = ["maça", "banana", "morango"]
#frutas[1] = "uvas"
# print(frutas[1])

#adicionando novos elementos append() adiciona no final

# frutas.append("manga")

# #removendo usando remove() ou pela posição pop()
# frutas.remove("banana")
# #frutas.remove("banana")
# frutas.pop(0)

# #IMPORTANTE for em lista
# for fruta in frutas:
#     print(frutas)

# #saber o tamanho da lista len()
# print(len(frutas))

#exemplo pratico lista de pedidos
pedidos = []
#adicionando pedidos com append
pedidos.append("Hamburger")
pedidos.append("Pizza")
pedidos.append("Refrigerante")

for pedido in pedidos:
    print(pedido)

#lista com numeros
numeros = [10, 20, 30, 40]
total = 0
for numero in numeros:
    total += numero
print(total)

#lista dentro de lista

cardapio = [
    ["Hamburger", 15],
    ["Pizza,", 30],
    ["Refrigerante", 8]
]

print(cardapio[0][0])
print(cardapio[0][1])