estoque = {
    "maca" : 10,
    "banana" : 8,
    "pera" : 0
}

fruta = input("Fruta a verificar: ")
print(fruta)
if fruta in estoque and estoque[fruta] > 0:
    estoque[fruta] -= 1
    print(f"{estoque[fruta]}")
else:
    print("O item está esgotado.")