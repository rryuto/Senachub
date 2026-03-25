convidados = []

for i in range(3):
    amigo = input("Digite o nome do convidado: ")
    convidados.append(amigo)
    

convidados.insert(0, "Silvio Santos")

remover = input("Remover um amigo: ")
convidados.remove(remover)

for i in convidados:
    print(i)

print(len(convidados))