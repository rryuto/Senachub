boletim = {
    "materia": "Matematica",
    "p1" : 8,
    "p2" : 7,
    "p3" : 10
}

total = 0
media = 0
for chave, valor in boletim.items():
    if chave != "materia":
        total += valor

media = total/(len(boletim)-1)

print(f"A média final de {boletim["materia"]} é {media:.2f}")