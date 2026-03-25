agenda = []

for i in range(3):
    nome = input("Adicione nome a agenda:\n")
    telefone = input("Adicione telefone a agenda:\n")

    agenda.append({
        "nome": nome,
        "telefone": telefone
    })

print(agenda)