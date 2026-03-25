compras = []
i = 0
for i in range(3):
    item = input("Digite o produto: ")
    compras.append(item)

for i, compra in enumerate(compras, start = 1):
    print(i, "-", compra)